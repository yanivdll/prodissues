Title: Just A Couple Of Emacs Keybindings
Date: 2016-02-23 00:00
Author: yaniv
Category: emacs
Tags: emacs, keybinding
Slug: intertesting-keybindings-in-emacs
Status: published

Every now and then I'll type something in Emacs with a certain goal,
just to find that I get something completely different from what I've
intended.

When in org file, I tried to convert a list item to a sub-header. The
keybinding to make this conversion is `C-c *`. But when I (thought I)
typed it, instead of getting a sub-header, a new buffer opened at the
bottom of the frame - a calculator:


![emacs-calc-mode.png](http://media.prodissues.com.s3.amazonaws.com/images/2016/02/emacs-calc-mode.png)

<span class="figure-number">Figure 1:</span> Calc mode

## view-lossage

I had no idea how did *that* happen, and luckily recalled a [tip I
got](https://www.reddit.com/r/emacs/comments/3w46xu/how_did_i_get_here_command/cxt6w6r), on how to move back in time using the `view-lossage` command, which
display last 300 input keystrokes. Doing so, I found that instead of
`C-c *`, I typed `C-x *`.

So now I know (and hopefully remember) that:

1.  There's a calculator[^1] in Emacs, bound to
    `C-x *`
2.  `C-h l` is a useful way to track back clumsy keystrokes

[^1]:Not that I had any doubts there is, just didn't think to look for it
just yet. There are so many other "to-learn" things on my list...

