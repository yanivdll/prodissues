Title: Emacs GPG For Dummies
Date: 2016-02-16 00:00
Author: yaniv
Category: emacs, geeking
Tags: gpg, mu4e, offlineimap, security
Slug: emacs-gpg-for-dummies
Status: published

I've [set up mu4e](https://prodissues.com/2016/02/adding-mu4e-support-to-emacs.html), and have my Gmail credentials stored in two files:

1.  `.offlineimaprc` - this file is used by Offlineimap to connect to my
    Gmail and sync my inbox with mu4e.
2.  `.authinfo` - that file stores my Gmail credential, and used by
    Emacs to send emails.

<!--more-->

Unfortunately, both of those files are plain text, and though I’m not a
security freak, I’m uncomfortable storing my passwords out in the open.
So, I went ahead to find out how to encrypt them. Most of the tutorials
I read were too technical, and covered much more than my simple usecase.
It’s not that I couldn’t follow theme, but I know I wouldn’t have
retained the information, and able to retract my steps if I needed to in
the future.

My goal with this post was to create a simple guide on how to install
gpg, generate a key, and use it in mu4e. I failed... I thought I will be
able to it non-technical for the most part, but once getting to
configure Emacs and mu4e to work with gpg, I had to delve into some
heavy configuration, which included the creation of a python script to
work along Offlineimap... The good thing is that this guide *will* help
you get Emacs and mu4e work with an encrypted version of a `.authinfo`
file, and your credentials will remain secret.

Now that our expectations are set, and assuming you're up for the ride,
lets start this journey.

## Installing GPG

``` sh
~ $ brew install gpg
```


Let's make sure gpg was installed:

``` sh
~ $ gpg --version
```


![gpg--version.png](http://media.prodissues.com.s3.amazonaws.com/images/2016/02/gpg--version.png)

<span class="figure-number">Figure 1:</span> gpg version information
along with the list of supported algorithms


Now really, the most informative source of information is gpg's help. Go
ahead and skim it:

``` lisp
~ $ gpg -h
```

## Create a key

``` sh
~ $ gpg --gen-key
```


There’s a simple wizard that lets you set the encryption type, and asks
for your name, email address and other comments. Those details will be
associated with your key.

Next, you’ll be asked to create a passphrase. This is like the password
to your secret key. If you lose it, you’ll have no access to any of the
information encrypted with this key. So don’t ever lose it…

Here’s how this flow looks like:


``` sh
~ $ gpg --gen-key
gpg (GnuPG) 1.4.19; Copyright (C) 2015 Free Software Foundation, Inc.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Please select what kind of key you want:
   (1) RSA and RSA (default)
   (2) DSA and Elgamal
   (3) DSA (sign only)
   (4) RSA (sign only)
Your selection? 1
RSA keys may be between 1024 and 4096 bits long.
What keysize do you want? (2048) 
Requested keysize is 2048 bits   
Please specify how long the key should be valid.
         0 = key does not expire
      <n>  = key expires in n days
      <n>w = key expires in n weeks
      <n>m = key expires in n months
      <n>y = key expires in n years
Key is valid for? (0) 
Key does not expire at all
Is this correct? (y/N) y

You need a user ID to identify your key; the software constructs the user ID
from the Real Name, Comment and Email Address in this form:
    "Heinrich Heine (Der Dichter) <heinrichh@duesseldorf.de>"

Real name: Jane Roe            
Email address: jane@example.com
Comment: lorem ipsum           
You selected this USER-ID:
    "Jane Roe (lorem ipsum) <jane@example.com>"

Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? O
You need a Passphrase to protect your secret key.    

We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
..........+++++
.+++++
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
..........+++++
...+++++
gpg: key 86B62C98 marked as ultimately trusted
public and secret key created and signed.

gpg: checking the trustdb
gpg: 3 marginal(s) needed, 1 complete(s) needed, PGP trust model
gpg: depth: 0  valid:   2  signed:   0  trust: 0-, 0q, 0n, 0m, 0f, 2u
pub   2048R/86B62C98 2016-02-17
      Key fingerprint = 42FD C031 BD51 4CC8 7C02  EA14 35D4 80A2 86B6 2C98
uid                  Jane Roe (lorem ipsum) <jane@example.com>
sub   2048R/8C0D5E5D 2016-02-17

~ $
```


Now that you've created a key, you can go ahead and sign the `.authinfo`
file.

## Sign and encrypt the `.authinfo` file[^1]

``` sh
~ $ gpg -se .authinfo
```


You'll be asked for your passphrase. Enter it, and the `.authinfo` will
be signed, and renamed to `.authinfo.gpg`

[EmacsWiki](https://www.emacswiki.org/emacs/GnusAuthinfo) suggests to
limit permission to this file. I find it important:

``` sh
~ $ chmod 600 .authinfo.gpg
```

Back in Emacs, there are couple of changes we need to make in order for
mu4e to start working with the `,authinfo.gpg` file. I wish I read [this
gist](https://gist.github.com/areina/3879626) before, because it covers
those changes succinctly, but here is a summary of those modifications:

## Changes to `.offlineimaprc` 

Two additions:

1.  A reference to a python file where you'll store a function to fetch
    your credentials from the `.authinfo.gpg` file
2.  Under the `[Repository Remote]` section add the call to the
    `get_password_emac` function

Here's how your `.offlineimaprc` file will look like afterwards:


``` lisp
[general]
accounts = Gmail
maxsyncaccounts = 3
pythonfile = ~/.offlineimap.py

[Account Gmail]
localrepository = Local
remoterepository = Remote

[Repository Local]
type = Maildir
localfolders = ~/Maildir
[Repository Remote]
type = IMAP
remoteuser = yanivdll@gmail.com
remotehost = imap.gmail.com
remotepasseval = get_password_emacs("imap.gmail.com", "yanivdll@gmail.com", "993")
ssl = yes
sslcacertfile = /usr/local/etc/openssl/certs/ca-bundle.crt
maxconnections = 1
realdelete = no
```


## Add a `.offlineimap.py` file

This file will define the `get_password_emac` function:


``` python
#!/usr/bin/python
import re, os

def get_password_emacs(machine, login, port):
    s = "machine %s login %s port %s password ([^ ]*)\n" % (machine, login, port)
    p = re.compile(s)
    authinfo = os.popen("gpg -q --no-tty -d ~/.authinfo.gpg").read()
    return p.search(authinfo).group(1)
```


## Changes to mu4e config {#orgheadline6}
----------------------


Lastly, in your Emacs config, under the mu4e smtp settings, add a
reference to the encrypted auth file:


``` lisp
...
(setq message-send-mail-function 'smtpmail-send-it
      starttls-use-gnutls t
      smtpmail-starttls-credentials
      '(("smtp.gmail.com" 465 nil nil))
      smtpmail-auth-credentials
      (expand-file-name "~/.authinfo.gpg")
      smtpmail-default-smtp-server "smtp.gmail.com"
      smtpmail-smtp-server "smtp.gmail.com"
      smtpmail-smtp-service 465
      smtpmail-debug-info t)
...
```


Now, you're emails should be sent using the `.authinfo.gpg` file. Go on
and try it[^2]. Note that before actually sending the email, Emacs will ask for your pass-phrase[^3]

## Extras

### Backup private key

I stored all the information related to my gpg key, as well as a backup
file in my [1password](https://agilebits.com/onepassword). Here's how I
created the key backup:


``` sh
~ $ gpg --export-secret-keys --armor jane@example.com > jroe-privkey.asc
```


**Important:** Make sure to store the output file in a secure place; it
contains your private key in plain text.


### Encrypt text in Emacs

1.  Mark the text you would like to encrypt
2.  Run `M-x epa-encrypt-region`
3.  Mark the key you would like to use for encryption

Now the encrypted text will replace the original, plain, text:


![encrypted-text.png](http://media.prodissues.com.s3.amazonaws.com/images/2016/02/encrypted-text.png)

<span class="figure-number">Figure 2:</span> `M-x epa-encrypt-region`
will encrypt a region of text in Emacs


### Decrypt text

To decrypt a message, or a file you've encrypted:

1.  Mark the text you would like to decrypt (you'll have to mark also
    the header and footer of the message)
2.  Run `M-x epa-decrypt-region`
    <div class="figure">

    ![decrypt-text.png](http://media.prodissues.com.s3.amazonaws.com/images/2016/02/decrypt-text.png)

    <span class="figure-number">Figure 3:</span>
    `M-x epa-decrypt-region` will decrypt a region of text in Emacs

    </div>

3.  Enter your pass-phrase
4.  Emacs will ask if you want the decrypted text to replace the
    original text. If you choose "No", it will open the text in a
    second window.


![decrypted-text-2.png](http://media.prodissues.com.s3.amazonaws.com/images/2016/02/decrypted-text-2.png)

<span class="figure-number">Figure 4:</span> The decrypted text in a
second window

That's it. If you're interested in more than the basics that I went
through above, try the links bellow.

 

## Reference

-   [Gnupg - documentation](https://www.gnupg.org/documentation/howtos.html)
-   Using gpg in emacs - [EasyPG Assistant user’s manual](https://www.gnu.org/software/emacs/manual/html_mono/epa.html#Quick-start)
-   [Fedora Wiki pages](https://fedoraproject.org/wiki/Creating_GPG_Keys#ExportCLI) - GPG essentials
-   [EmacsWiki - GnusAuthinfo](https://www.emacswiki.org/emacs/GnusAuthinfo)
-   [Tricotism - EasyPG for Emacs on OS X, or sometimes Emacs doesn’t load the env paths you might expect](http://danzorx.tumblr.com/post/11976550618/easypg-for-emacs-on-os-x-or-sometimes-emacs)
-   [ubuntu forums](http://ubuntuforums.org/showthread.php?t=2155060) Encrypting and decrypting a message

[^1]: Made an edit here (initially, I only signed the file, without encrypting
it). Thanks [/u/aminab](https://www.reddit.com/user/aminb) for [the
correction](https://www.reddit.com/r/emacs/comments/46fi6f/adding_mu4e_support_to_emacs_part_two_configuring/d04szm3).

[^2]: If you still have the `.authinfo` file, rename it. Once we see that mu4e
sends emails using the encrypted version of the auth file, we can
dispose this, decrypted, version of it.

[^3]: If Emacs asks for your passphrase too often, you might find this
[comment in Reddit](https://www.reddit.com/r/emacs/comments/45lx1s/adding_mu4e_support_to_emacs_the_hard_way/d01b1hu), by [/u/aminb](https://www.reddit.com/user/aminb), helpful.
