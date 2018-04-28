Title: Adding mu4e Support To Emacs
Date: 2016-02-12 00:00
Author: yaniv
Category: emacs
Tags: email, mu4e
Slug: adding-mu4e-support-to-emacs
Status: published

Couple of months ago[^1] I started to use Emacs
as my secondary email client; the primary one remains Gmail's web
interface. Bringing my Gmail account to Emacs wasn't as smooth sail as I
hoped it to be, but I'm happy with the results so far.

<!--more-->

## Why use Emacs for emails?

-   Because ~~I~~ Emacs can.
-   Because when writing a serious email (one with more than two lines),
    I usually draft it in an editor first. Now that this editor is
    Emacs, it makes sense to do the editing *and* the sending parts
    in it...
-   Because I want org support for my emails
-   And, because [these images](https://www.google.com/search?q=emacs+email%5C&client=safari&rls=en&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjSnqe8ys_JAhXH2D4KHYPAD4kQ_AUIBygB&biw=1496&bih=1003#tbm=isch&q=emacs+email) makes emails look way cooler in Emacs than in any other client.

## Choosing an email client

I went back and forth between mu4e and gnus, and finally took [Dhavan
Vaidya's](http://codingquark.com/setting-up-gnus-in-emacs/) advice to
pick one and just move on with it. Unlike him, though, I chose mu4e,
mainly because its focus on search.

So here we go - implementing mu4e in Emacs. For a quick and dirty
checklist, follow the first part, which summaries the steps to get mu4e
working. If you're more of an FPS person, and interested in the details,
read through the second part, which journals my steps as well as the
errors I encountered and their fixes.


> Note: The [Mu4e official manual](http://www.djcbsoftware.nl/code/mu/mu4e/index.html) is great, as long as everything works flawlessly. In my case, though, I run through every problem and error possible. So if you want to install mu4e, I recommend you'll start with the manual. If you get stuck, or encounter a problem, you might find the solution here.


## The short story

1.  Install [Homebrew](http://brew.sh/)
2.  Install [offlineimap](http://offlineimap.org/)
3.  Configure offlineimap to point to the IMAP server you would like to
    connect to.
4.  Run offlineimap for the first time to download your IMAP folder from
    the remote server.
5.  Get mu from git: <https://github.com/djcb/mu>
6.  Run mu to index and load the messages into Emacs.
7.  Configure your Emacs init file to connect with mu4e and customize
    the client.
8.  On Emacs, run - `M-x mu4e`


## The details
According to the manual, mu4e is only a client, or an interface to my
emails, and does non of the fetching, storing, editing or sending them
on its own.

> This leaves mu4e to concentrate on what it does best: quickly finding
> the mails you are looking for, and handle them as efficiently as
> possible.

Mu4e should, therefore, be complemented with the other components to
work. My hope is that installing all those packages won't be too big of
a hassle... And with that, let's move on to the installation checklist.

The [mu4e
manual](http://www.djcbsoftware.nl/code/mu/mu4e/Installation.html#Installation) is thorough
and informative, but I'm not sure how to install mu and make it
available in Emacs. I also don't understand what I should use to manage
the IMAP repository for me. I'm getting confused...

Searching for unofficial documentation, or a blog post for some extra
hand holding, I find [this
one](http://blog.developwithpassion.com/2013/05/02/getting-up-and-running-with-a-sane-mutt-setup/)
by Jean-Paul. It turned out that I should install offlineimap from brew,
as well as SQLite, which will store messages' states:



### Installing offlineimap 

``` sh
// install brew
$ brew install wget
```


``` sh
//install offlineimap
$ brew install offlineimap
```


Done. Next - modify the offlineimap configuration file. Here's my Gmail
setup:


``` sh
[general]
accounts = Gmail
maxsyncaccounts = 3

[Account Gmail]
localrepository = Local
remoterepository = Remote

[Repository Local]
type = Maildir
localfolders = ~/Maildir

[Repository Remote]
type = IMAP
remotehost = imap.gmail.com
remoteuser = USERNAME@gmail.com //change with your email
remotepass = PASSWORD         //change with your password
ssl = yes
sslcacertfile = /etc/ssl/certs/ca-certificates.crt
maxconnections = 1
realdelete = no
```


This `sslcacertfile` line I got from
[stack-overflow](http://superuser.com/questions/927632/configuring-offlineimap-for-gmail-ssl-error),
after getting an error when trying to load `offlineimap`.

Offlineimap still refuses to load. Apparently the folder specified in
`sslcacertfile` doesn't exist in my computer, and offlineimap can't
connect to my Gmail account. More research, and I finally find this
helpful, ["How can I use sslcertfile"](http://lists.alioth.debian.org/pipermail/offlineimap-project/2014-August/004916.html),
article. Here's the gist of it:

1.  Download the ca-cert bundle
    from [sourceforge](https://downloads.sourceforge.net/project/machomebrew/mirror/curl-ca-bundle-1.87.tar.bz2).
2.  Copy the `ca-bundle.crt` file to `/usr/local/etc/openssl/certs/`
3.  I didn't have to, but if it still doesn't work, try
    running `/usr/local/opt/openssl/bin/c_rehas` , so openssl can take
    note of the new certificate.
4.  Update the `sslcacertifile` parameter with the new folder:


``` sh
sslcacertfile = /usr/local/etc/openssl/certs/ca-bundle.crt
```


Offlineimap is finally working, and downloading my emails.

Waiting... I have 45977 messages to sync, so it's going to take some
time. I'll do other stuff in the meantime.

Damn! In my stupidity I closed the lid of my laptop, and when opened it
again found that the offilneimap sync process hangs. I kill it, and try
to run it again. I can't - another error. The fix - delete the
`Gmail.lock` file:


``` sh
$ rm .offlineimap/Gmail.lock
```


Running `offlineimap` again. Works this time.


![offlineimap-sync.png](http://media.prodissues.com.s3.amazonaws.com/images/2016/02/offlineimap-sync.png)


While my repository is syncing, I switch to configure mu and mu4e.


### Installing mu

First, I clone the mu repository and install libtool (I have no idea
what it does, just that it's required for building mu)


``` sh
$ git clone https://github.com/djcb/mu.git
$ brew install libtool
```



Next, build mu:



``` sh
$ cd mu
mu/$ autoreconf -i && ./configure && make
```


Once the offlineimap process ends, I run mu to index my emails, which
located at the `/Maildir` folder, as defined in the `~/.offlineimaprc`
file.


``` sh
/usr/local/Cellar/mu/mu/$ ./mu index
```


Here's the result:


![mu-index.png](http://media.prodissues.com.s3.amazonaws.com/images/2016/02/mu-index.png)


We're making progress here...


### Emacs config

Now I have to setup mu4e (mu for Emacs, I assume...). In my
[config](https://github.com/yanivdll/.emacs.d/blob/master/config.org#mu4e)
file, I add the following settings, taken almost as-is from mu4e manual:


```lisp
(add-to-list 'load-path "/usr/local/Cellar/mu/mu4e")
(setq mu4e-mu-binary (executable-find "/usr/local/Cellar/mu/mu/mu"))
(require 'mu4e)

;; default
(setq mu4e-maildir "~/Maildir")
(setq mu4e-drafts-folder "/[Gmail].Drafts")
(setq mu4e-sent-folder   "/[Gmail].Sent Mail")
(setq mu4e-trash-folder  "/[Gmail].Trash")
(setq mu4e-refile-folder  "/[Gmail].All Mail")

;; don't save message to Sent Messages, Gmail/IMAP takes care of this
(setq mu4e-sent-messages-behavior 'delete)

;; (See the documentation for `mu4e-sent-messages-behavior' if you have
;; additional non-Gmail addresses and want assign them different
;; behavior.)

;; setup some handy shortcuts
;; you can quickly switch to your Inbox -- press ``ji''
;; then, when you want archive some messages, move them to
;; the 'All Mail' folder by pressing ``ma''.

(setq mu4e-maildir-shortcuts
    '( ("/INBOX"               . ?i)
       ("/[Gmail].Sent Mail"   . ?s)
       ("/[Gmail].Trash"       . ?t)
       ("/[Gmail].All Mail"    . ?a)))

;; allow for updating mail using 'U' in the main view:
(setq mu4e-get-mail-command "offlineimap")
```

Note that I had to add the first two lines, because without them Emacs
doesn't know about mu4e, and about where to find the mu executable. I
know it because I tried evaluating the config many times time, without
mu4e loading...

And now, finally, when I run `M-x mu4e`, Hooray!


![mu4e\_first\_screen.png](http://media.prodissues.com/images/2015/12/mu4e_first_screen.png)


Now that I have all my emails in Emacs, I'll start learning the
ins-and-outs of mu4e, and customize it further.


## Update

Couple of weeks ago, Gmail asked that I change my password, due to a
suspicious login attempt to my account. I did, and updated the password
in my `.offlineimaprc` file. But since then, although incoming emails
worked fine, I was unable to send emails from mu4e, and kept
getting this error message:

``` sh
smtpmail-send-it: Sending failed: 535-5.7.8 Username and Password not accepted. Learn more at
535 5.7.8  https://support.google.com/mail/answer/14257 64sm1217489qhf.40 - gsmtp in response to AUTH PLAIN AHlhbml2ZGxsADExODc3WWFu
```


I spent days trying to sort this problem out. I went through [Google's
detailed checklist](https://support.google.com/mail/answer/14257) numerous times, read and posted in Google's support forum, looked in stack-overflow, but
found nothing to help me solve that error.

Finally, I found an EmacWiki's article about [sending mail](https://www.emacswiki.org/emacs/SendingMail) in Emacs. It mentions the `$(HOME)/.authinfo` file and I suspected it had something to do with
the problem I had... I opened this file, and lo and behold... it had my
Gmail credentials, including my old password in it. I updated the
password and now I can use mu4e to send emails again.

[^1]: I was writing this post while going through the installation process,
although I published it just now.