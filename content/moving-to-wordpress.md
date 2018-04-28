Title: Moving to Wordpress
Date: 2016-01-26 00:00
Author: yaniv
Category: blogging
Tags: pelican, Wordpress
Slug: moving-to-wordpress
Status: published


![pelican-to-wordpress.png](http://media.prodissues.com.s3.amazonaws.com/images/2016/02/pelican-to-wordpress.png)

That was quick.

Couple of weeks ago I wrote about thinking to [move my blog to
Wordpress](http://prodissues.com/2016/01/should-i-keep-using-pelican-or-move-to-wordpress.html).
Since then, I've used Wordpress[^1] in
conjunction with my static blog, and published posts to both sites. This
experiment helped me to reaffirm the pros and cons of using Wordpress,
especially the part about concentrating on writing rather than site
administration. During those two weeks I posted more, and became
comfortable working with, and in, Wordpress.

When I realized that I started to publish first to my dummy Wordpress
blog, and then reluctantly to my static blog, I made the decision to
switch. Yesterday I completed the migration.

Following is the checklist I've used to manage the migration. It helped
me going through the process with no downtime, and no prodissues :-)

<!--more-->

#### Decide between hosted an self-hosted

Initially I wanted to keep it as simple as possible, by paying for the
basic plan on [Wordpress.com](https://store.wordpress.com/plans/). I
wanted to avoid technical setup. Eventually, though, I went the
self-hosting route for one simple reason - I wanted to keep the same URL
format I had with the static site, but Worpress.com doesn't let you
define the permalink format.


#### Select a hosting provider

There are tons of comparisons between every possible hosting provider,
enough to get me confused about the pricing and the different features.
Since my site is small and simple, and without a lot of traffic, I
decided to take the economical route, and go with a shared hosting
service. I then narrowed the list to Godaddy and Bluehost, and finally
decided on Bluehost[^2], mainly because it's
[endorsed by Wordpress](https://wordpress.org/hosting/).

#### Local installation of WP

Wordpress famous claim for 5 minute installation isn't a cliche. I just
had to follow [this guide](https://codex.wordpress.org/Installing_WordPress_Locally_on_Your_Mac_With_MAMP).

#### Import all of my posts to the local install

My plan to export and import an RSS feed from my static blog to
Wordpress didn't work. WordPress RSS importer didn't recognize my
Pelican generated RSS feed, so I had to spend some time researching for
an alternative.

My posts are written in one of two formats - markdown or
[org-mode](http://orgmode.org/). Migrating the org-mode based posts was
easy, using Emacs' [org2blog](https://github.com/punchagan/org2blog/)
package. Pushing the markdown files was a little trickier. Eventually,
with the help of [this stack-overflow
answer](http://emacs.stackexchange.com/q/5465/10150), I converted those
markdown posts into org-mode, using pandoc. I had to make a little bit
of cleaning[^3] to the output, but overall that
process wasn't too complicated.

#### Connect to Bluehost

Now that I had my local installation of Wordpress up and running with
all my posts, it was time to set Wordpress on Bluehost.

Logging-in to my Bluehost panel for the first time was intimidating. The
endless list of tools got me thinking that I might end up doing even
more site administration work than I did before. I hoped, though, that
this will be the case only during the initial setup[^4], and that I will not have to log in to that panel again after
I deploy my site.


![bluehost-cpanel.png](http://media.prodissues.com.s3.amazonaws.com/images/2016/02/bluehost-cpanel.png)

<span class="figure-number">Figure 2:</span> The cPanel - lots of tools,
though I had to use only few to get my site live


#### Connect to WP with a temporary URL

When I signed up with Bluehost, I got an email with a list of temporal
IPs and ftp configuration. This way I could set up my Wordpress blog
before having to point my domain to it. At first, I wasn't able to
access my temporary URL, even after reading [this detailed
article](http://www.expression-web-tips.com/accessing-bluehost-domains-from-a-temporary-web-address/).
It probably took time for the URL to be activated and link to my
account, because I was able to access it eventually (after couple of
hours) without doing anything special.

As soon as I connected to the temporary URL, a Wordpress installation
process started, and 5 minutes later I had Wordpress installed on my
production environment. Exciting!

The first thing I've noticed when logging in to my fresh self-hosted
Wordpress was this gaudy green icon - the Mojo market place. I didn't
know what Mojo is, and didn't care to know. I just wanted it out of my
dashboard. Googling it, I
[found](https://wordpress.org/support/topic/how-do-i-remove-mojo-marketplace-from-admin-header)
that it's just a plugin that can be removed. Removed it I
had [^5].

#### Set FTP access

With a little hand holding from the Bluehost support team, I was able to
connect to my temporary URL via ftp. Here's the FileZilla configuration
I had to set:

![filezilla-setup.png](http://media.prodissues.com/images/2016/01/filezilla-setup.png)

<span class="figure-number">Figure 3:</span> My FileZilla Configuration
- note the non-default Encryption type


FTP connection will be useful later on, when I'll need to push my local
environment and database to production.


#### Themes that I like

Back to my localhost Wordpress, I need to chose a theme, and get ready
to push everything to Bluehost. Here's the list of themes I liked:

-   [Big brother](https://theme.wordpress.com/themes/big-brother/)
-   [Twenty twelve](https://theme.wordpress.com/themes/big-brother/) - I
    don't like the font though.
-   [P2](http://p2theme.com/)
-   [Everyday](https://theme.wordpress.com/themes/everyday/) (75\$)
-   [Twenty Sixteen](https://wordpress.org/themes/twentysixteen/)
    (that's the one I chose.)


#### Import the local installation to the hosting service

I used [Bluehost's excellent
guide](https://www.bluehost.com/blog/wordpress-2/faq-how-do-i-move-my-wordpress-website-to-bluehost-1787/)
for that. At first, I messed things up by not following it step-by-step
- I pushed my local database before copying my local Wordpress
installation and overriding that on the host. As a result I had to run
the Wordpress installation on Bluehost again. Not a big deal, but a
reminder about the complexity behind the scene...


#### Set the permalink format


My blog is up and running on a temporary URL. This post for example was
accessible with the following URL (not anymore, though):

`http://69.195.124.143/~prodissu/2016/02/moving-to-wordpress.html`

I now had to make sure that my URLs are formatted correctly. That was
easily done within the wp-admin. The setting is under
setting-&gt;permalink.


![wp-admin-set-permalink.png](http://media.prodissues.com.s3.amazonaws.com/images/2016/02/wp-admin-set-permalink.png)

<span class="figure-number">Figure 4:</span> Setting the permalink
format


Now I had to make sure that when I switch to Wordpress, all of my
existing posts will maintain the same URL. So, I run through a sample of
posts, replaced the temporary part of the URL (the
`http://69.195.124.143/~prodissu/` in the example above), which led to
the Wordpress installation, with my domain name. Doing so I've expected
to land on the same post on my static, and still live, site. When I made
sure this is the case, I was ready for the final part - the cut-off.

#### Figure how to transfer my domain

My domain registrar is Godaddy, and my static site was running on AWS
S3. To move my domain to link to Bluehost instead of AWS, I had to
change the configuration of the nameservers on Godaddy. [Here's a
guide](https://my.bluehost.com/cgi/help/432) for how to do that.

One small consideration at that point - I have a bucket on S3 dedicated
to all the media file I use in posts. I wanted to keep this bucket and
not move those media files into the Wordpress database. Just in case I
change my mind again, and decide to switch back to static blog at some
point. I also kind of wanted to keep that neat workflow I created to
[upload media files to
S3](http://prodissues.com/2016/01/uploading-images-to-amazon-s3.html)...

To maintain that bucket and sub-domain, I had to [define a
CNAME](https://my.bluehost.com/cgi/help/559#add), now on the Bluehost
console.

With that, my site is up and running on Wordpress. Hooray!

There's only one open task left:

#### Import the disqus comments

I exported the comments from disqus, but didn't find a way to import
them into Wordpress.


## Helpful links

-   [Installing Wordpress Locally on Your Mac With
    MAMP](https://codex.wordpress.org/Installing_WordPress_Locally_on_Your_Mac_With_MAMP)
-   [Accessing Bluehost Domains and ftp from a Temporary Web
    Address](http://www.expression-web-tips.com/accessing-bluehost-domains-from-a-temporary-web-address/)
-   [Using Your Temporary URL with
    Wordpress](https://my.bluehost.com/cgi/help/wordpress_url)
-   [How Do I Transfer My Wordpress Website To
    Bluehost?](https://www.bluehost.com/blog/wordpress-2/faq-how-do-i-move-my-wordpress-website-to-bluehost-1787/)

[^1]: First, I created a blog in Wordpress.com. Then I installed Wordpress on
my local machine.

[^2]: So far I'm happy with Bluehost. I had to chat with their support twice,
once to help me with connecting to the ftp, and then to white-list my IP
for remote publishing. Support was prompt and helpful in both cases.

[^3]: I had to add the headers to the org file and fix some of the footnotes'
references.

[^4]: It's probably too early to answer this question, but since making the
cut-off, I didn't have to log in to the cPanel.

[^5]: I removed it so quickly, that I didn't even take a screen shot to
include here.
