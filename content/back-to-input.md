Title: Back To Input
Date: 2016-02-02 16:18
Author: yaniv
Category: emacs
Tags: configuration, fonts
Slug: back-to-input
Status: published

Now that I moved to Wordpress, I can finally set Emacs' font to
Input. Wait, *what*? what does an Emacs font has to do with WordPress?

<!--more-->

Well, in a previous post, I documented how to [modify fonts in
Emacs](http://prodissues.com/2015/11/changing-the-default-font-in-emacs.html).
However, I had to rollback the new font, because it broke Pelican's
org-reader plugin, which relied on Emacs' configuration. For some reason
it didn't like the new font, and decided it doesn't generate HTML files
until I revert to `Menlo`.

In fact, this is one of the reasons I gave up on Pelican. It was too
brittle. So now that I'm on WordPress, I'm free to configure Emacs
however I want. Here's how my new font looks like:

![](http://media.prodissues.com.s3.amazonaws.com/images/2016/02/emacs-input-font.png)
