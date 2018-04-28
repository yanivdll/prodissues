Title: Magit - My Simple Workflow
Date: 2016-10-05 20:30
Author: yaniv
Category: emacs
Slug: magit-my-simple-workflow
Status: published

I still not fluent with Magit's terminology and workflow. Probably because I'm not using git in general too often. When I do, and when I try to use Magit as the interface, I usually get confused by the wealth of options and switches, and resort to the terminal.

Today I decided to give Magit yet another try. I read the this [Getting Started](https://magit.vc/manual/magit/Getting-started.html#Getting-started) guide, and now things makes much more sense. However, I can see how I forget what I've just read a week from now, so here's the gist of that, my simplest cheat-sheet:


## (Ma)git status:

`C-x g`


## (Ma)git add

For each unstage file:
`s`


## (Ma)git commit

`c c`

Type the commit note and then `C-c C-c` to create the commit.


## (Ma)git push

`p u`

Done. Now I can type `q` to close the Magit pop-up buffer, and be back on the file I was working on.