Title: Copy Git Changes to a New Branch
Date: 2015-11-12 05:00
Author: yaniv
Category: code
Tags: git
Slug: copy-git-changes-to-a-new-branch
Status: published

I'm still not fluent with git and version control. I manage repositories
for projects I'm working on, but sill have hard time managing my
changes, commits and branches.

For example, I'm currently working on integrating Emacs's org-mode
support to Pelican, a static web-page generator I use for this blog. I
was proud of myself for remembering to create a new branch when starting
the work. Somewhere in the middle of the integration, I drift away, and
started to explore a new idea - adding a commenting system to the site.
Before I knew it I was already working on it. Unfortunately, not only
that I didn't work on that feature in a dedicated branch, I was still on
the branch I created for the org integration.

I wondered if there is a way to take the changes I made since the last
commit, and pour them over into a new branch. Luckily, there is. Here's
how, thank to [this answer in
stack-overflow](http://stackoverflow.com/a/4746696/1424287):

> You can simply check out a new branch, and then commit:

``` bash
git checkout -b my_new_branch 
git commit
```

> Checking out the new branch will not discard your changes.

Tried it and it worked.
