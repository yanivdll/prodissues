Title: Changing the default font in Emacs
Date: 2015-11-30 05:00
Author: yaniv
Category: emacs
Tags: emacs
Slug: changing-the-default-font-in-emacs
Status: published

Josh Stella wrote a [delightful
post](https://blog.fugue.co/2015-11-11-guide-to-emacs.html) about how he
uses Emacs, not necessarily for development work. I found quite a few
configuration tips, and already implemented few of them. One of those
tweaks is using the Input font family. Visiting
[fontbureau](http://input.fontbureau.com/) made me want this font too!

I thought it will be as simple as `copy-paste` (I'm still not used to
the appropriate `kill-yank` terminology) Josh's configuration. It wasn't
- after reloading my init, the font didn't pick up.

Few experimentations later, though, and it *did* work. First, I had to
download and install the font in my mac, dahhh... Then, I had to modify
the name of the font (Josh used `InputSerif`; I had to change it to
`Input`). Here's my configuration:



``` lisp
;; set up fonts for different OSes. OSX toggles to full screen.
(setq myfont "Input")
(cond
((string-equal system-name "ygilad.local")
 (set-face-attribute 'default nil :font myfont :height 144)
 (toggle-frame-fullscreen)))
```


Indeed, it looks beautiful. Here's a screen grab of this post in Input:
![emacs\_with\_input\_font.png](http://media.prodissues.com/images/2015/11/emacs_with_input_font.png)

There's still one problem - this modification to my config broke the
org-reader plugin, and I can't export my org files to Pelican. Sadly,
I'll have to resort to the default font (Menlo), until I figure out a
fix.
