Title: Bunch of Emacs Tweaks
Date: 2015-12-04 05:00
Author: yaniv
Category: emacs
Tags: emacs, tweaks
Slug: bunch-of-emacs-tweaks
Status: published


## Comment\\Uncomment a Line

Few useful commands for commenting\\uncommenting lines in emacs. Taken
from the [Emacs
tutorial](http://www.gnu.org/software/emacs/manual/html_node/emacs/Comment-Commands.html).
Sure, I can go back to the manual, but I want to ducument and keep them
here, for quicker reference.

> `M-;` Insert or realign comment on current line; if the region is
> active, comment or uncomment the region instead (comment-dwim).
>
> `C-u M-;` Kill comment on current line (comment-kill).
>
> `C-x ;` Set comment column (comment-set-column).
>
> `C-M-j` `M-j` Like RET followed by inserting and aligning a comment
> (comment-indent-new-line). See Multi-Line Comments.
>
> `M-x comment-region`

Mastering this command takes me one step further into Emacs, as it used
to be one of those functionalities that keep drawing me back to Sublime
Text.


## Quick reload of init.el file {#orgheadline2}


I'm constantly customizing my emacs. I have an `init.el` file, but most
of the configuration in a more literal way, in an org [config
file](https://github.com/yanivdll/.emacs.d/blob/master/config.org).

When I make changes to Emacs settings, I need to reload the init file
activate the changes. So far, I typed `C-x C-f` to find the init file
and then `M-x [RET] eval-buffer` to reload it. Repeating this flow
hundreds of times became annoying.

A quick inquery [in IRC](http://prodissues.com/2015/11/leap-into-the-past-irc.html), and now
I know that I can call `load-file` and give it the name of the file I
would like to load. Having a function to load a file, means that I can
wrap it with my own function, and reload my init file with a customized
keybind.

And with the help of [this
answer](http://stackoverflow.com/a/12558095/1424287) at stack-overflow,
I came up with the following shortcut to reload my Emacs configuration:


```lisp
(global-set-key (kbd "<f6>") (lambda() (interactive)(load-file "~/.emacs.d/init.el")))
```



## New line bellow

I wondered if there's a command to creat a new line bellow the line my
point is on. Here's what I found in
[superuser](http://superuser.com/a/331661/525565):

`C-e C-m` - go to the end of the line, create a new line and move the
point to that line.

or

`C-e C-j` - same as the command above, only that the point will indent
if neccessery.

There is also a keybind for creating a new line above the current line,
and move the point to that line - `C-a C-o`.



## Quick Open a specific file

Now days I start most of my writing in my [draft
file](http://prodissues.com/posts_drafts/). I need a quick way to access
this file, whether I'm in Emacs or any other application. I know Emacs
has the concept of registers, which are special memory slots, that can
be accessed with a command. Those registers can store any type of data,
such as strings, integers, files and paths.

It's time to learn how to work with them. When thinking about it, there
are other files that I would have liked to access quicker, such as the
[init.el](https://github.com/yanivdll/.emacs.d/blob/master/init.el) or
[config.org](https://github.com/yanivdll/.emacs.d/blob/master/config.org).

Google's first search result was EmacsWiki. Again, it proved to be a
great source of information, had I wanted to confuse myself. So I
passed. The second result was from [Emacs
tutorial](https://www.gnu.org/software/emacs/manual/html_node/emacs/File-Registers.html#File-Registers),
which again proved to be clear, concise and informative.

Here are the commands for storing a filename in and loading it from a
register:



``` lisp
(set-register r '(file . name))
```


For example,


``` lisp
(set-register ?r '(file . "~/Dropbox/Notes/posts/pages/posts_drafts.org"))
```



To load this file, I should type `C-x r j r`

In the code examples above, `r` is the name of the register. It can be
replaced with any character.

And to see what's stored in a specific register:


``` lisp
M-x view-register RET r
```


Again, `r` is the register I'm querying.

## Change cases

  `M-l`        Convert following word to lower case (downcase-word).

  `M-u`        Convert following word to upper case (upcase-word).

  `M-c`        Capitalize the following word (capitalize-word).

  `C-x C-l`    Convert region to lower case (downcase-region).
  
  `C-x C-u`    Convert region to upper case (upcase-region).

