Title: Drafts
Date: 2015-11-15 00:00
Author: yaniv
Category: drafts
Slug: drafts
Status: published

<div id="content">

<div id="table-of-contents">

Table of Contents
-----------------

<div id="text-table-of-contents">

-   [What's this?](#orgheadline1)
-   [Emacs](#orgheadline70)
    -   [Switching buffer focus](#orgheadline2)
    -   [Using calendar](#orgheadline3)
    -   [Indirect buffer](#orgheadline4)
    -   [Working with Markdown](#orgheadline5)
    -   [Defining writing modes](#orgheadline8)
    -   [Multiple cursor](#orgheadline9)
    -   [Dictionary and Thesaurus](#orgheadline11)
    -   [Draft mode](#orgheadline12)
    -   [Adding a dictionary](#orgheadline13)
    -   [Commands to move between frames](#orgheadline14)
    -   [Setting Emacs on Mac for Python](#orgheadline17)
    -   [Load dired-x by default   <span class="tag"><span
        class="emacs">emacs</span></span>](#orgheadline18)
    -   [Bidirectional Editing](#orgheadline19)
    -   [Orgmode](#orgheadline57)
    -   [Themes](#orgheadline60)
    -   [Experimitation with Spacemacs](#orgheadline61)
    -   [Add several folders to deft](#orgheadline65)
    -   [<span class="todo nilTODO">TODO</span> Undo tree
        mode](#orgheadline66)
    -   [How to modify emacs window so the buffer have right and left
        margins](#orgheadline67)
    -   [How do I change windows layout back and forth](#orgheadline68)
    -   [Running several instances of Emacs](#orgheadline69)
-   [Prodissues](#orgheadline74)
    -   [Adding a tag cloud](#orgheadline71)
    -   [Add inline footnotes](#orgheadline72)
-   [Wordpress](#orgheadline77)
    -   [Updating wordpress - checklist](#orgheadline75)
    -   [Importing comments from disqus](#orgheadline76)
-   [Code](#orgheadline90)
    -   [Parsing emails in Python](#orgheadline78)
    -   [Connecting to Elasticsearch (or ELK
        with Python)](#orgheadline84)
    -   [Integrating Sphere with Alfred](#orgheadline85)
    -   [Adding scheduled job in mac](#orgheadline86)
    -   [How to figure out the size of a folder from
        terminal](#orgheadline87)
    -   [Writing a python script for Lorem Ipsum](#orgheadline88)
    -   [Parsing a json file with logstash](#orgheadline89)
-   [Work](#orgheadline106)
    -   [Elastic Search is amazing](#orgheadline95)
    -   [Getting Feedback from users and customers](#orgheadline104)
    -   [Fearute ownership](#orgheadline105)
-   [Omakase](#orgheadline108)
    -   [From Idea to Vision and Back to an MVP](#orgheadline107)
-   [Workflows](#orgheadline112)
    -   [Process mail](#orgheadline109)
    -   [Remove HTML Files With Hazel](#orgheadline110)
    -   [Stitch two images together](#orgheadline111)
-   [Other](#orgheadline128)
    -   [So much going on...](#orgheadline113)
    -   [Don't Build a Dominos Pizza Company](#orgheadline117)
    -   [Webarchive](#orgheadline123)
    -   [It's not about you. It's about the topic.](#orgheadline124)
    -   [Mechanical Keybords](#orgheadline126)
    -   [POST - how to make yourself look dumb](#orgheadline127)

</div>

</div>

<div id="outline-container-orgheadline1" class="outline-2">

What's this? {#orgheadline1}
------------

<div id="text-orgheadline1" class="outline-text-2">

This is an org mode based file where I draft all my posts. I keep this
file and post it because it helps me work on several posts in paralel,
and add to drafts as I go. Once I'm done with a post, I move it to a new
file, which is then pushed as a stand alone post.

</div>

</div>

<div id="outline-container-orgheadline70" class="outline-2">

Emacs {#orgheadline70}
-----

<div id="text-orgheadline70" class="outline-text-2">

</div>

<div id="outline-container-orgheadline2" class="outline-3">

### Switching buffer focus {#orgheadline2}

<div id="text-orgheadline2" class="outline-text-3">

Sometimes I feel, much like
[/u/imnothere123puff](https://www.reddit.com/r/emacs/comments/49of20/installed_emacs_started_tutorial_cn_cp_cf_cb_now/?ref=share&ref_source=link),
that to use Emacs efficiently, I need few more hands. Take buffer and
windows navigation for example - the default keybinding to circle
through open buffers is `C-x o`; to switch to the next buffer -
`C-x right`.

Those keybindings are annoying. Not only that they require two steps for
one action, but they also hurting your cadence of
typing^[1](#fn.1){#fnr.1 .footref}^.

I wanted to change this behavior and define different keybindings that
will be easier to type and fit better with my mental model, which
associate `tab` with switching between different areas on the screen. I
took it also as an opportunity to establish a workflow for customizing
various behaviors of emacs.

Here's the workflow I came up with:

-   Define what the outcome behavior should be. In this case, I wanted a
    comfortable keybinding to circle through
    -   In my case I wanted to:
        -   Define a keybinding to switch focus among open windows
            within the same frame
        -   Define a keybinding to navigate accross buffers
-   Is there already a keybinding for that function? if yes, look for
    the function this keybinding trigger. \`C-h k RET \[keybinding\]\`
    will describe exactly what happens when you run the sequence
    of keys.
-   Locate the function that is triggered when the keybinding used.
-   Go to your init file, where the keybinding of your liking should
    be configured.
-   Insert this elips snippet anywhere^[2](#fn.2){#fnr.2 .footref}^
    <div class="org-src-container">

    ``` {.src .src-emacs-lisp}
    (global-set-key [(control tab)] 'other-window)
    ```

    </div>

This is a good example for how to start customizing emacs. I first
looked for what

</div>

</div>

<div id="outline-container-orgheadline3" class="outline-3">

### Using calendar {#orgheadline3}

<div id="text-orgheadline3" class="outline-text-3">

The goal here is to use emacs to:

1.  View my gcal in Emacs
2.  Sync gcal with Emacs
3.  View org cal
4.  Sync org entries in gcal

</div>

</div>

<div id="outline-container-orgheadline4" class="outline-3">

### Indirect buffer {#orgheadline4}

<div id="text-orgheadline4" class="outline-text-3">

When working on an org file, many times I zoom into one of the sections
to focus on it. At times I would like to zoom out just for a second, but
not loose my point. In those instances, the indirect buffer is what I
would like to use. I learned about it from the excellent video \[link\]
here, but I have hard time to remember how to do it. So here's a quick
checklist.

</div>

</div>

<div id="outline-container-orgheadline5" class="outline-3">

### Working with Markdown {#orgheadline5}

<div id="text-orgheadline5" class="outline-text-3">

When on my desktop, most of what I write is in orgmode. But when you
think about it, while org is text based, and a superset of markdown,
it's not really portable - you can't write or read it anywhere else
that's not Emacs.

So when I'm on my mobile, I take notes using Drafts and Editorial
(mainly the former though). I write my notes in markdown and then export
them to Dropbox. So when I'm back to my desktop and want to continue
workin on the notes that I've started, I prefer to continue edit them in
Markdown.

Here are few of the commands I frequently use:

1.  Live preview - `C-c C-c l` - this will open another window of eww
    and present the rendered html output of the markdown I'm working on.
    It's not "live live", but updates every time you hit save.
2.  

And by the way - I use Jason Blevins exellent
[markdown-mode](https://github.com/jrblevin/markdown-mode/), and learned
everything that I'm covering here from the documentation he put
together.

And by the way, not that I have anything against org, in fact I started
to use emacs because of it and don't look back, but I like the simlicity
of markdown, and this package reminds me of its charm.

</div>

</div>

<div id="outline-container-orgheadline8" class="outline-3">

### Defining writing modes {#orgheadline8}

<div id="text-orgheadline8" class="outline-text-3">

</div>

<div id="outline-container-orgheadline6" class="outline-4">

#### Draft writing mode {#orgheadline6}

</div>

<div id="outline-container-orgheadline7" class="outline-4">

#### Editing Mode {#orgheadline7}

</div>

</div>

<div id="outline-container-orgheadline9" class="outline-3">

### Multiple cursor {#orgheadline9}

<div id="text-orgheadline9" class="outline-text-3">

Recently I moved my site from Pelican to Wordpress. As part of this move
I also dumped disqus and now use WordPress commenting system. I didn't
find a good way to import my comments from disqus to WordPress, and can
get myself to do this arduous work manually.

In parallel, I recently got curious to try and find use to multiple
cursors. Today I watched the amazing [Emacs
Rocks!](http://emacsrocks.com/e13.html) episod featuring multiple
coursors. Not only that I thought that this is a feature I *must*
muster, I now had a usecase to experiment with.

So here we go. I'm trying to use multiple cursors to convert disqus'
comments xml export to something WordPress can import.

</div>

<div id="outline-container-orgheadline10" class="outline-4">

#### Reference {#orgheadline10}

<div id="text-orgheadline10" class="outline-text-4">

-   [Github](https://github.com/magnars/multiple-cursors.el)
-   [Emacs Rocks!](http://emacsrocks.com/e13.html)

</div>

</div>

</div>

<div id="outline-container-orgheadline11" class="outline-3">

### Dictionary and Thesaurus {#orgheadline11}

<div id="text-orgheadline11" class="outline-text-3">

This is a summary of the packages and functions suggested in this reddit
thread, and the solution I moved forward with.

</div>

</div>

<div id="outline-container-orgheadline12" class="outline-3">

### Draft mode {#orgheadline12}

<div id="text-orgheadline12" class="outline-text-3">

One of the reasons I'm using Emacs is that it removes a lot of the
distructions I would have otherwise have. Being completely text based,
and keyboard driven, my hands are always in a typing position, so I have
to concentrait less on stuff that are not writing.  
Yet, I still get distructed often. For example, I will struggle with
spelling a certain word, think of a better way to phrase a sentence I
wrote in a previous paragraph, or spend time with finding a better way
to say something. Those small distructions, while relevant to writing
(it's not that I open a browser and go to reddit or anything, I'm still
in writing mode), but they cut the line of thought, and might take my in
tangles (link to the post about writing).

Long story short, I learned about draft-mode, a minor mode that once
enabled let you do nothing but writing. It emulating a typewriter, so
all you can do is move forward. No way back, no way to delete, lookup a
word or do anything that is not keep typing.

I found this entriguing, especially as a way to brain dump a though or a
first draft. Sure, the outcome is messy to say the least, but being able
to consentrait only on squeesing out this thought is invaluable.

So, here's what I did, and what I found out:

</div>

</div>

<div id="outline-container-orgheadline13" class="outline-3">

### Adding a dictionary {#orgheadline13}

</div>

<div id="outline-container-orgheadline14" class="outline-3">

### Commands to move between frames {#orgheadline14}

<div id="text-orgheadline14" class="outline-text-3">

Now that I've started to use mu4e for my emails, I want to keep my inbox
open in a seperate frame, and the documents that I'm working on in
another. I'm looking for a simple way to move from one frame to the
other.

</div>

<div id="outline-container-orgheadline15" class="outline-4">

#### Reference {#orgheadline15}

<div id="text-orgheadline15" class="outline-text-4">

<https://www.gnu.org/software/emacs/manual/html_node/emacs/Frame-Commands.html>

</div>

</div>

</div>

<div id="outline-container-orgheadline17" class="outline-3">

### Setting Emacs on Mac for Python {#orgheadline17}

<div id="text-orgheadline17" class="outline-text-3">

</div>

<div id="outline-container-orgheadline16" class="outline-4">

#### What do I try to achive with this integration? {#orgheadline16}

<div id="text-orgheadline16" class="outline-text-4">

-   Python syntax highlighting
-   Auto-complition, including for default and 3rd party packages
-   Evaluate code in a seperate, horizontal buffer (like I did
    in CodeRunner)

I recently moved all my writing to emacs, and since I do, or should I
say - try to do some python coding - I searched for a tutorial on how to
customize emacs as a Python editor.

Before emacs, the litle Python I wrote, was done with CodeRunner and
Sublime Text, but mostly in the out-of-box IDLE. Each one of these
enviornemt lacked something, so I didn't have any strings attached when
I decided to move my coding to emacs.

I started to google things like "setting emacs for python on mac", but I
didn't find one tutorial that could walk me through the entire
configuration. I did find some useful sprinkles of tips and information.

anything relevant. So instead of keep looking, I decided to figure it
out myself, and write a tutorial on it, so other in my position have a
better start than I had.

</div>

</div>

</div>

<div id="outline-container-orgheadline18" class="outline-3">

### Load dired-x by default   <span class="tag"><span class="emacs">emacs</span></span> {#orgheadline18}

<div id="text-orgheadline18" class="outline-text-3">

There are times when I want to take a peek at a file's underlying
folder. I might want to open another file from that folder, do a quick
rename or just get myself oriented about where the file I'm working on
lives.

I learned that there is a
[keybinding](http://www.cs.washington.edu/acm/tutorials/editors/dired-refcard.gnu.pdf)
for it, but that I can use this keybinding only if I have dired-x
enabled.

After some googling I learned that dired-x is part of emacs, and there
is no need to install anything. I needed, however, to enable it
somehow^[3](#fn.3){#fnr.3 .footref}^. A little more digging till I found
in the [dired
manual](http://www.gnu.org/software/emacs/manual/html_node/dired-x/Optional-Installation-Dired-Jump.html)
the following code snippet that will auto load the package:

<div class="org-src-container">

``` {.src .src-emacs-lisp}
(autoload 'dired-jump "dired-x"
  "Jump to Dired buffer corresponding to current buffer." t)

(autoload 'dired-jump-other-window "dired-x"
  "Like \\[dired-jump] (dired-jump) but in other window." t)

(define-key global-map "\C-x\C-j" 'dired-jump)
(define-key global-map "\C-x4\C-j" 'dired-jump-other-window)
```

</div>

And now, `C-x C-j` will open the folder of the current file. `C-x 4 C-j`
will open the folder in a different window.

</div>

</div>

<div id="outline-container-orgheadline19" class="outline-3">

### Bidirectional Editing {#orgheadline19}

<div id="text-orgheadline19" class="outline-text-3">

I rarly write in hebrew, but now that I've started to use emacs for
emails, sometime I'll have to answer an email in my native language.
Writing in Hebrew is a challange because of its right-to-left nature
that tend to break everything... for years I couldn't use mac for that
reason.

It turned out to be an easy enought to set Emacs to respect my Hebrew,
and even to make it play nice when it's surrounded by other languages.

</div>

<div id="outline-container-orgheadline20" class="outline-4">

#### References {#orgheadline20}

<div id="text-orgheadline20" class="outline-text-4">

-   Emacs manual -
    <https://www.gnu.org/software/emacs/manual/html_node/emacs/Bidirectional-Editing.html>
-   

</div>

</div>

</div>

<div id="outline-container-orgheadline57" class="outline-3">

### Orgmode {#orgheadline57}

<div id="text-orgheadline57" class="outline-text-3">

</div>

<div id="outline-container-orgheadline21" class="outline-4">

#### Pelican + Orgmode   <span class="tag"><span class="orgmode">orgmode</span> <span class="pelican">pelican</span></span> {#orgheadline21}

<div id="text-orgheadline21" class="outline-text-4">

For awhile now I'm trying to create a workflow for writing and
publishing a blog post. Here is a list of my requirments:

1.  The source should be in a text based format, so text, markdown or
    org, each will be good.
2.  I would like to be able to manage and edit from one folder,
    preferable the folder where I have all my notes.

Until recently, I wrote my articles in markdown. When I was done with
the article, I copied it to the content folder in my pelicon based blog.
I then run \`make html\` to process the source into a static html, and
when I was sutisfied with the piece, I would have pushed the pelican
output folder to aws, where my blog is hosted.

Rarely was I satisfied with the piece when copying it to the pelican
folder. Many times I had to do some final editing. Since I edited my
original text in a a markdown editor, and the code for the site in
Sublime Text, I was inclined to the open the article in Sublime, cause
mose of the times I was already there, messing with other code, and do
the changes on the spot. In that broken workflow, I was left with two
copies for each of my posts. Most of the times these copies weren't
identicle. So, once copying a post into pelican, I couldn't trust that I
can edit the original post, but had to go back to the content folder,
and open the post there. That turned my central note folder useless when
it came to managing my posts.

I recently started to work with emacs, and move a lot of my text based
activities to it. And so working on the site and on articles are done at
the same place.

I still want to keep a version of my posts in dropbox though, so I still
want to have some kind of export workflow in place. This is also true
since I want to start writing my posts in org, which isn't supported out
of the box by pelican.

So after a long introduction, the problem I'm trying to solve is

</div>

-   [](){#orgheadline22}How to export a post from my dropbox folder to
    the content folder in Pelican?
    <div id="text-orgheadline22" class="outline-text-6">

    I want to have the editable format of the article available only in
    one place. What I've experienced so far was that I started an
    article in my notes folder, at first through nvAlt and then moved to
    emacs and deft. When I thought I was done and moved the article to
    the content

    </div>

-   [](){#orgheadline23}Configure Org mode to publish (in general)
    <div id="text-orgheadline23" class="outline-text-5">

    This is a straight forward customization. I had to follow
    the tutorial.

    </div>

-   [](){#orgheadline24}Configure the html export to pelican
-   [](){#orgheadline25}Importing html file into Pelican
    <div id="text-orgheadline25" class="outline-text-5">

    It turns out importing to pelican is harder than I expected.

    But, the export doesn't work as I thought it will. The problem was
    that the header that Pelican expect, wasn't translated in a way it
    can work with. So as a result, the file that was created in the
    Pelican content folder wasn't compiled to the output.

    </div>

-   [](){#orgheadline26}Trying an import to markdown
    <div id="text-orgheadline26" class="outline-text-5">

    HTML publishing didn't work for now. Before trying to work on the
    main problem, which is the header of the file, I'll try to do a
    markdown export and see that it works. If it does, I might keep it
    like that and work with org to markdown.

    Markdown export doesn't work well also. Two issues that I had:

    -   Org add the outline of the post on top. This is annoying, but
        I'm sure I can find the solution easily, but not at the moment.
    -   The bigger issue is that I can't seem to be able to pass the
        head meta tags that Pelican expects to get and process.

    Hitting the wall. Markdown export doesn't work either.

    </div>

-   [](){#orgheadline27}Trying the org-export
    <div id="text-orgheadline27" class="outline-text-5">

    I tried to follow [this
    article](http://nhoffman.github.io/borborygmi/getting-started.html)
    but wasn't able to make it work. I cloned [the
    repository](https://github.com/nhoffman/org-export) and made
    the export. But still, the header meta wasn't included in the
    output HTML. Now the post mentioned another utility that was
    "easily" created to do that, but it's not included, so what's the
    point in the article...?

    So, just as I'm about to give up, I found a way that allows me to
    pass header parameters to the html output. Now, I can have org
    communicate with pelican. I don't like this solution that much,
    because it clatters my org file with markup, but this is something I
    can live with.

    [reference to how the header tag looks
    like](https://github.com/fniessen/org-html-themes/blob/328260286c89aa0b8a4f3bd6be902de50da696bf/setup/theme-bigblow-local.setup)

    Now, I'm only missing the syntax highlighting in the output file,
    the one that goes to the site.  
   Found a solution for that. I had to include htmlize, and now I can
    export or files into html! yay.

    Next problem to solve:  
   Footnotes are shown awkwardly. I've looked for a setting that will
    allow me to remove the footnote header. Found this variable "Org
    Footnote Section" and removed the "Collect footnotes under heading"
    to nil. I'm going to restart emacs and see what happens.
    Finger crossed...

    Oh wow. I found the tresure! I went to emacs settings and searched
    for "org html export". I found that I can control evry element of
    the export, including how the footnotes section will be formated.
    But I'm greedy, and now looking for header construction, in a way
    that I can include tags or meta headers in markdown or org format,
    and have them translate into header tags. This way I won't have to
    include ugly markups in my source files.

    Found [another
    article](https://pavpanchekha.com/blog/org-mode-publish.html) that
    was helpful in understanding how ord export works, and include some
    tips on setting up the publishing hook for git - export the site
    whenever I do a commit. I might get back to it at some point.

    Ok, I think I got to the end of the journey. I found out that after
    all the trubles that I went through, there is a [plugin for
    pelican](https://github.com/getpelican/pelican-plugins/tree/master/org_reader).
    How stupid am I not to figure it out. And more than that - the
    plugin set in my computer all this time... so reading [this
    post](http://msnyder.info/posts/2013/12/introducing-pelicorg/)
    walked me through the setup, and now I can have my org files
    directly in my pelican content directory. Halelluya!!!

    One last obsecal. That damn syntaxy highlighting thing went
    away again. I think the first article I read had a solution
    for that. I'll go check it out again.

    Yes, Yes, Yes! adding this simple (require 'color-theme-github) did
    the trick, and now my implementation is done.

    And now that I can have my org files directly in pelican, I can
    actually save also this pipeline posts file there, only in
    dradt mode.

    </div>

-   [](){#orgheadline28}References
    <div id="text-orgheadline28" class="outline-text-5">

    -   [Publishing orgmode files to
        HTML](http://orgmode.org/worg/org-tutorials/org-publish-html-tutorial.html)
    -   [Using org with
        Jekyll](http://orgmode.org/worg/org-tutorials/org-jekyll.html) -
        This is a good reference to setup the publishing of the org
        files to the content folder in Jekyll. It seems that with
        pelican, the setup will be very similar.
    -   mention the good tutorial
        \[here\](<http://nhoffman.github.io/borborygmi/getting-started.html>)

    </div>

-   [](){#orgheadline29}Merging Drafts Into One Orgmode File
    <div id="text-orgheadline29" class="outline-text-5">

    Up until now my writing workflow included creating new file for each
    post I started to write. I gave those drafts a file name starting
    with "post -". This way it was easy to sift through my posts ideas
    in nvAlt.

    Recentely, I moved to emacs, and was drawn into orgmode. I now write
    everything in org. Org is the best outliner I worked with, and so
    when I read \[Sacha's\]() tip on managing all her posts-to-be in one
    org outline, I got curious. I started by outlining several new ideas
    that I had, and eventually decided to merge my entire collection of
    drafts into one org file.

    </div>

-   [](){#orgheadline30}Why is it a good idea?
    <div id="text-orgheadline30" class="outline-text-5">

    I started to do it, but realised quickly that it will be lame to
    manually copy and paste the content of some 30 files into one file.
    Inspired by the "Automate The Boring Stuff With Python" that I read
    couple of months ago, I thought this might be a good opportunity to
    implement what I learned. And so I went ahead and wrote the
    following script that scan my draft files, create a new outline
    header from the filename (minuse the "post - "prefix) and append the
    content of each file under the relevant header.

    </div>

-   [](){#orgheadline31}Exporting a post from org mode to pelican
    <div id="text-orgheadline31" class="outline-text-5">

    I'm trying to move my blog posts from markdown to org.

    Starting with an outline that is part of a bigger org file that
    holds all my drafts.  
   In my Dropbox folder, I keep all my notes in a Notes/ folder. In
    that folder I created a sub-folder for all my posts.

    I then killed the sub-tree that held my draft and yanked it into a
    new org file in the post folder.

    Now, before exporting this post to an HTML in the pelican folder, I
    needed to add some meta data, especially date, which pelican is
    finicky about.

    Ok, reporting failure on that for now. I didn't find a good
    reference to how I do the export to HTML, and what org headers I
    need to use to make the transition. And so I did for now, an export
    to markdown, saved the markdown in the Pelicon content folder and
    published from there.

    This is a bad compromise, because I had to do some modifications to
    the markdown document, such as adding

    </div>

</div>

<div id="outline-container-orgheadline32" class="outline-4">

#### Link to a specific subtree in another org file {#orgheadline32}

</div>

<div id="outline-container-orgheadline33" class="outline-4">

#### Refile a Subtree to a New Org File {#orgheadline33}

<div id="text-orgheadline33" class="outline-text-4">

I manage all my drafts for new posts in one file. This is an insperation
from Sacha.  
So now, what I want to be able to do is refiling a subtree, which
represent post's draft, to a new file that will turn to the final post.

I googled it, and
[here](http://superuser.com/questions/373617/re-file-outline-tree-into-new-org-mode-file)
is the result I got. Reading through it makes me think that like
integrating org with pelican, this isn't going to be a quick
configuration, but will require some more involvemnt. I will therefore
stash this modification, cause I have some more important things to work
on at the moment...

</div>

</div>

<div id="outline-container-orgheadline34" class="outline-4">

#### Pass Org Header Parameters to Pelican {#orgheadline34}

<div id="text-orgheadline34" class="outline-text-4">

After a long process of trying to integrate Org with Pelican, I landed
on Pelican's [org\_reader
plugin](https://github.com/getpelican/pelican-plugins/tree/master/org_reader).
It works well and allows me to write my posts in orgmode. But as I gain
more posts, I want to categorize and orginize them better.

Org\_reader is quit limiting in the amount of header properties it
allows to map. In fact it support only the `title`, `category`, `date`
and `author`. In fact, it maps org's `category` to pelican's `tags`,
while both org and pelican has the accurate property names for both tags
and category.

So, I decided to expand this plugin to support more properties (maybe
all?). I don't know yet how to do it, whether I should simply change the
package localy on my computer and risk breaking it when an update to
this plugin is available, or do it the proper way - forking (either to
add the missing functionality and then making a pull request, or use it
as a starting point to an alternative version of the plugin).

While the second route makes much more sence, it also mean that a quick
and dirty solution isn't an option. And that means I have to learn, at
least some, elisp. I'm not sure I'm ready for it at the moment.

So, I'll put that project on a hold for now, and I'll start by setting
my emacs environment to work with elisp - development and debugging.
Yeah, I already see how I'm going to be sucked into learning elisp in no
time...

**10 minutes later:**  
I forked the org\_reader repository...

**2 hours later:**  
Started to read ["Learning Elisp the Hard
Way"](https://github.com/hypernumbers/learn_elisp_the_hard_way).

</div>

</div>

<div id="outline-container-orgheadline39" class="outline-4">

#### Links in orgmode {#orgheadline39}

<div id="text-orgheadline39" class="outline-text-4">

</div>

-   [](){#orgheadline35}Create an external link
    <div id="text-orgheadline35" class="outline-text-5">

    The format for a link in org is:

    ``` {.example}
    [[link_url][description]]
    ```

    I found it tricky to use this convention. The way I inclined to
    create links is to first construct he governing brackets, so to get
    something like^[4](#fn.4){#fnr.4 .footref}^. I'll then go and add
    the description and lastly the url.

    The problem is that when I enter the description part, and move the
    point outside the description's enclosed paranthesees, the link
    changes, and all I can see is the description. In that view I can't
    modify the url part of the link.

    I found the answer in [Org Mode Compact
    Guide](http://orgmode.org/guide/Link-format.html#Link-format)

    > Org will recognize plain URL-like links and activate them as
    > clickable  
   > links. The general link format, however, looks like this:
    >
    > ``` {.example}
    > [[link][description]] or alternatively [[link]]
    > ```
    >
    > Once a link in the buffer is complete (all brackets present), Org
    > will change the display so that ‘description’ is displayed instead
    > of `[[fsdf]]` and ‘link’ is  
   > displayed instead of `[[link]]`. To edit the invisible ‘link’
    > part, use  
   > C-c C-l with the cursor on the link.

    So now, instead of constructing the markup for a link, I simply type
    'C-c C-l RET' at the point where I want the reference link to
    be inserted. In the prompt that shows in the mini-buffer, I enter
    the link's url and the description. I

    </div>

-   [](){#orgheadline36}Remove a link
    <div id="text-orgheadline36" class="outline-text-5">

    I created a link, but want to remove the link, and keep only
    the description. Here's a function that I'll have to add to my
    init file.

    <div class="org-src-container">

    ``` {.src .src-emacs-lisp}
    (defun afs/org-replace-link-by-link-description ()
        "Replace an org link by its description or if empty its address"
      (interactive)
      (if (org-in-regexp org-bracket-link-regexp 1)
          (let ((remove (list (match-beginning 0) (match-end 0)))
            (description (if (match-end 3) 
                     (org-match-string-no-properties 3)
                     (org-match-string-no-properties 1))))
        (apply 'delete-region remove)
        (insert description))))
    ```

    </div>

    I got this script from an answer in
    [stack-overflow](http://emacs.stackexchange.com/a/10714).

    </div>

    -   [](){#orgheadline37}The want:
        <div id="text-orgheadline37" class="outline-text-6">

        I have a link that I've defined. Now I want to remove the link
        part, and remain only with the link's lable. So for example, if
        I have [google](http://google.com) linke, and I want to remove
        the underline url, but still keep the string google.

        </div>

        -   [](){#orgheadline38}Solution
            <div id="text-orgheadline38" class="outline-text-7">

            I bumped into a function that's doing it in the past. I'm
            not sure if I documented it or not, but I should
            return\\search for it and grab the code...

            </div>

</div>

<div id="outline-container-orgheadline40" class="outline-4">

#### Forking the org\_reader plugin {#orgheadline40}

<div id="text-orgheadline40" class="outline-text-4">

The goal is to be able to export org files simlessly to pelican. I want
to have all the meta tags that Pelican allows, synced from org in
Emacs.  
I will build on top of the org\_reader plugin, and then decide if I make
a pull request, or add my own version with attribution to the other
plugin.

Here's what I did:

</div>

-   [](){#orgheadline41}Forked the org\_reader plugin
-   [](){#orgheadline42}Copied the plugin to a new folder -
    ort\_to\_pelican
-   [](){#orgheadline43}Created a test blog in pelican
    <div id="text-orgheadline43" class="outline-text-5">

    I don't want to make changes that harm my current implementation.
    Want to create a clean environment to experimintations.

    </div>

-   [](){#orgheadline44}Find the touching point with org meta
    <div id="text-orgheadline44" class="outline-text-5">

    I found the part of the code where the plug in connect with the org
    export meta data. I switched the json to get static values, just to
    make sure I'm touching the right spot.

    Here's the before:

    <div class="org-src-container">

    ``` {.src .src-python}
    ...
    metadata = {'title': 'json_output['title']',
                        'tags': json_output['category'] or '',
                        'slug': slug,
                        'author': json_output['author'],
                        'date': json_output['date']}

            parsed = {}
            for key, value in metadata.items():
                parsed[key] = self.process_metadata(key, value)

            return json_output['post'], parsed
    ```

    </div>

    And the after:

    <div class="org-src-container">

    ``` {.src .src-python}
    ...
     metadata = {'title': 'TITLE - This is a test of a static json',
                        'tags': 'emacs',
                        'slug': 'This is a test slug',
                        'author': 'Yaniv',
                        'date': '2015-11-11'}

            parsed = {}
            for key, value in metadata.items():
                parsed[key] = self.process_metadata(key, value)

            return json_output['post'], parsed
    ```

    </div>

    I changed the attributes of the json that probably feeds the pelican
    with static values. The resulted article showed those
    static attributes.

    Next.

    </div>

-   [](){#orgheadline45}Read the meta tags from the org post
    <div id="text-orgheadline45" class="outline-text-5">

    Instead of waiting for the meta tags to be exported from org, I'll
    go ahead and fetch them directly from the org file. The reason for
    going around the org export is that it's apis only expost subset of
    entities, while I want to support more properties.

    </div>

-   [](){#orgheadline46}Implemented the parsing method
    <div id="text-orgheadline46" class="outline-text-5">

    This method read the org file.  
   It read lines and if a line is a property line, it breaks it into
    a dictionaty.

    </div>

-   [](){#orgheadline47}Need to map the resulting dictionary with the
    pelicon terminology.
-   [](){#orgheadline48}Resources
    <div id="text-orgheadline48" class="outline-text-5">

    -   Pelican documentation
        -   [Contributing a
            plugin](https://github.com/getpelican/pelican-plugins/blob/master/Contributing.rst)
        -   [Contributing
            guidelines](http://docs.getpelican.com/en/latest/contribute.html#using-git-and-github)
            and Contribution quality standards
    -   A blog post about [pelican plugin
        tests](https://github.com/getpelican/pelican-plugins/tree/master/org_reader)
    -   Documentation for the [org\_reader
        plugin](https://github.com/getpelican/pelican-plugins/tree/master/org_reader)
    -   [Creating a site with Pelican and
        org-mode](http://nhoffman.github.io/borborygmi/getting-started.html#sec-1-1)

    </div>

</div>

<div id="outline-container-orgheadline49" class="outline-4">

#### Inserting an inline image with org {#orgheadline49}

<div id="text-orgheadline49" class="outline-text-4">

I'm trying to add an image from a url that will show inline (and not as
a link). What I found in the org manual is how to do it with a local
file, but it seems to not work with remote file, or with using `http:`
instead of `file:`.

Here's what I found so far:

Ok, I found this answer in
[stack-overflow](http://stackoverflow.com/questions/9639425/org-mode-export-as-html-inline-images-displayed-and-linked)
that worked for me. I think I made the wrong search, and the information
that I got was about how to show images inline in an org file. While
this might be useful, it wasn't exactly what I needed. I will explore
the inline image display later on.

</div>

</div>

<div id="outline-container-orgheadline50" class="outline-4">

#### Orgmode - Presentation With Reavel {#orgheadline50}

<div id="text-orgheadline50" class="outline-text-4">

I want to be able to write my presentation with text. I don't like doing
my presentation with any of the ordinary apps because I end up spending
most of my time on the look and feel rather than on the content, and on
what I want to achive from the presentation.

As I move more and more parts of my life to org, running presentations
using it sounded like a good idea. I looked for plugins that I can use
for that task. I used landslide with markdown before, the experience was
ok. What I found for org, which work also with markdown, is Reveal. So I
decided to give it a try.

</div>

-   [](){#orgheadline51}Installation and configuration
    <div id="text-orgheadline51" class="outline-text-5">

    -   Clone reveal into \~/dev/reveal. Here's a [link to the latest
        version](https://github.com/hakimel/reveal.js/releases/latest).
    -   Configure org-reveal package in Emacs
        -   First try: Add the following to my init file
            <div class="org-src-container">

            ``` {.src .src-emacs-lisp}
            (use-package ox-reveal
            :ensure t
            :config
            (setq org-reveal-root "~/dev/reveal/reveal.js"))
            ```

            </div>

            <p>
            That didn't work. When evaluating my init file, it
            complained that the package isn't available.
        -   Second try: Clone the org-reveal repository into my
            \~/.emacs.d/lisp/ folder (that's were I place packages that
            I downloaded manually, i.e. not from one of the
            package hubs). That didn't work either. My init loaded
            without problem, but the org-reveal package didn't.
        -   Third try: I commented the use-package config, and used the
            ordinary require:
            <div class="org-src-container">

            ``` {.src .src-emacs-lisp}
            (require 'ox-reveal)
            ```

            </div>

            <p>
            This time it worked.
    -   Try it out - Seems that the package is now loading. So I created
        a test presentation, like this one:
        <div class="org-src-container">

        ``` {.src .src-org}
        * Slide 1
        * Slide 2 
        ** Slide 2.1
        ** Slide 2.2
        * Slide 3
        ```

        </div>

    I then called `org-reveal-export-to-html`, but got an error
    `Symbol's function definition is void: org-export-get-referenc`. Not
    sure why... Taking a step backward, to read the documentation again,
    and see where did I take the wrong step.

    </div>

-   [](){#orgheadline52}Reference
    <div id="text-orgheadline52" class="outline-text-5">

    -   [Create HTML5 Presentations Easily With Emacs and
        Reveal.js](http://jr0cket.co.uk/2013/10/create-html5-presentations-emacs-revealjs.html.html)

    </div>

</div>

<div id="outline-container-orgheadline53" class="outline-4">

#### Add footnote within the same section {#orgheadline53}

<div id="text-orgheadline53" class="outline-text-4">

This way I can add footnotes to a post while still in draft stage and
page.

</div>

</div>

<div id="outline-container-orgheadline56" class="outline-4">

#### Latex {#orgheadline56}

<div id="text-orgheadline56" class="outline-text-4">

</div>

-   [](){#orgheadline54}Keybindings and tricks
    <div id="text-orgheadline54" class="outline-text-5">

    > Code within a paragraph.
    >
    > <div class="LATEX">
    >
    > All lines between these markers are exported literally
    >
    > </div>

    </div>

-   [](){#orgheadline55}Reference
    <div id="text-orgheadline55" class="outline-text-5">

    -   [Latex in the org
        manual](http://orgmode.org/manual/Quoting-LaTeX-code.html#Quoting-LaTeX-code)
    -   [Latex export from
        org](http://orgmode.org/worg/org-tutorials/org-latex-export.html)
    -   [Emacs org-mode examples and
        cookbook](http://ehneilsen.net/notebook/orgExamples/org-examples.html)
    -   [Latex reference - Hypertext Help with
        LaTeX](http://www.forkosh.com/latex/ltx-2.html)
    -   [Create new latex
        commands](https://www.sharelatex.com/learn/Commands)
    -   [How to write a LaTeX class file and design your own
        CV](https://www.sharelatex.com/blog/2011/03/27/how-to-write-a-latex-class-file-and-design-your-own-cv.html)

    </div>

</div>

</div>

<div id="outline-container-orgheadline60" class="outline-3">

### Themes {#orgheadline60}

<div id="text-orgheadline60" class="outline-text-3">

</div>

<div id="outline-container-orgheadline58" class="outline-4">

#### Flip between light and dark themes {#orgheadline58}

<div id="text-orgheadline58" class="outline-text-4">

I want to creat a function that flip between light and dark thems.

-   Choose the themes I want to flip through.
-   Create a variable that will hold the name of the current theme, so I
    can switch it with a keybinding.

</div>

</div>

<div id="outline-container-orgheadline59" class="outline-4">

#### Add Solarized theme to emacs {#orgheadline59}

<div id="text-orgheadline59" class="outline-text-4">

I fell in love with that theme.  
I installed the solarized theme from elpa (github repo
[here](https://github.com/bbatsov/solarized-emacs))  
This was very easy, but the problem was that the headers in org mode
didn't adhear to the theme.  
I tried this package:
<https://github.com/sellout/emacs-color-theme-solarized>, but couldn't
make init to load the theme correctly. I also didn't want to change my
path to themes to that theme's folder, because I might want to add more
themes to that path, and the `custom-theme-directory` doesn't seem to be
a list.

So now I found this post -
<https://blog.sleeplessbeastie.eu/2014/06/09/how-to-use-solarized-theme-in-emacs/>.  
I hope this article will be helpful. It wasn't.

Both Sacha's configuration, and the article I read didn't help. It
seemed that I have a cumborsum variable of the header that inherited
it's value, and overriden the theme.

Eventually, like many other questions, I found a solution in an answer
at [stack-overflow](http://emacs.stackexchange.com/a/16873/10150). I had
to use the first repo, and add this line to the init:

<div class="org-src-container">

``` {.src .src-emacs-lisp}
(setq solarized-scale-org-headlines nil)
```

</div>

</div>

</div>

</div>

<div id="outline-container-orgheadline61" class="outline-3">

### Experimitation with Spacemacs {#orgheadline61}

<div id="text-orgheadline61" class="outline-text-3">

-   Note taken on <span class="timestamp-wrapper"><span
    class="timestamp">\[2015-11-16 Mon 14:45\]</span></span>  
   Start

The other day I added @melpa\_emacs to my emacs twitter list, so now I
can see every new package or update that is submitted to melpa.

One of those packages is
[spaceline](https://github.com/TheBB/spaceline). I didn't know what it
is, but saw that it has many downloads (relatively). I was intrigued to
learn more. Realized it a package that imitates the look and feel of
spacemacs mode-line. Hmmm... Spacemacs. Should I try it? afterall it
aims to combine the benefites of vim and emacs. Since I use Evil mode, I
thought it might be a good idea to take spacemacs for a spin.

I was relactunt to do it in the past, because spacemacs is known for the
amount of packages it adds by default, and I liked the idea of
controling and growing the emacs installation and customization with me.
My curiosity won, and I cloned spacemacs.

I loaded it, but figured it will ential another phase of learning
completly new product, and decided it's not the right time for me to
start that journey. Especially as I'm starting to feel more comfortable
with emacs "vanilla".

So, I backed up the spacemacs folder and stashed it for now. I'll
probably want to get back to it at some point in the future. I hope that
by then I'll have more capacity to learn new things, and be even more
proficient with emacs.

</div>

</div>

<div id="outline-container-orgheadline65" class="outline-3">

### Add several folders to deft {#orgheadline65}

<div id="text-orgheadline65" class="outline-text-3">

</div>

<div id="outline-container-orgheadline62" class="outline-4">

#### Question {#orgheadline62}

<div id="text-orgheadline62" class="outline-text-4">

-   How do I pass a list of folders so deft search in them?

</div>

</div>

<div id="outline-container-orgheadline63" class="outline-4">

#### Answer {#orgheadline63}

<div id="text-orgheadline63" class="outline-text-4">

There is no way to specify more than one folder. The variable name hint
to that - it called setq deft-directory - note directory in singular
rather than plural^[5](#fn.5){#fnr.5 .footref}^

</div>

</div>

<div id="outline-container-orgheadline64" class="outline-4">

#### Reference {#orgheadline64}

<div id="text-orgheadline64" class="outline-text-4">

-   [Deft documentation page](http://jblevins.org/projects/deft/)

</div>

</div>

</div>

<div id="outline-container-orgheadline66" class="outline-3">

### <span class="todo TODO">TODO</span> Undo tree mode {#orgheadline66}

<div id="text-orgheadline66" class="outline-text-3">

Copied the setting from Sacha's config file -
<http://pages.sachachua.com/.emacs.d/Sacha.html#orgheadline158>  
Need to learn a little more how to use it.

</div>

</div>

<div id="outline-container-orgheadline67" class="outline-3">

### How to modify emacs window so the buffer have right and left margins {#orgheadline67}

<div id="text-orgheadline67" class="outline-text-3">

There is the set-left-margin, but this modify the actual text in the
buffer. I want to change the window, so it will not affect the actual
text within the buffer.

</div>

</div>

<div id="outline-container-orgheadline68" class="outline-3">

### How do I change windows layout back and forth {#orgheadline68}

<div id="text-orgheadline68" class="outline-text-3">

When I write documents, I want the document I'm working on to take the
entire frame. If I want to take a quick glimps to another file, or to
look for some related information, I want to open anotehr window within
the same frame. When I'm done, I want to go back to the previous layout
of single window.

Of course, `C-x 3` to open the 2 window and then `C-x 1` to get rid of
the window will do the same thing. But what if I want to keep the layout
as well as the documents the shown in each of the windows? what if I
want to quickly tuggle back and forth between those layouts?

The `C-x {n}` keybinding have no history. So if I open a second window,
it will open with the file I have on the initial window, and I'll have
to switch focus and open the second file. If I close the second window,
and then open it again, again it will open on the file shown on the
single window. Did I loose you with all the swiching back and forth? so
yeah, that's how I loos track of all the open files and where they are
when I switch from one to another.

So, what I'm looking for is a way to move between predefined frame
configurations, or way to save and go back to a layout that I already
created.

It took me awhile to articulate what I'm looking for. When I did, I
landed on this
[stack-overflow](http://stackoverflow.com/questions/2572950/preserve-window-layout-in-emacs)
thread, which was a usefull starting point.

From that answer, I learned about two packages:

1.  [Winner-mode](https://www.emacswiki.org/emacs/WinnerMode)

This is as simple as undo\\redo for windows layout. It's part of Emacs,
so no need to download the package or set use-package to load it.

I found it to be very usefull for cases when I want to go back and forth
between two layouts. This is what I was looking for originally. The
problem with this package seems to be that every action on the window
pushes into the undo stack. So if I'm on a certain file, open a new
file, split the frame into two vertical windows and in one of the
windows open a third file, I registered 3 actions to the undo ring. To
get to the first file that was shown on a single window, I have to run
the undo command 3 times. And to get back to the 2 layout (2 windows
with 2 differnet files), I'll have to redo 3 times. Not that convinient
or intuitive.

Actually, I might have to look at it again. If I go through the undo
ring, and get to say the 4th layout within the ring. Now when I redo,
I'll jump to the initial layout, the one I've started the undo at. Yet,
it will still take me another 4 undos to get back again to the second
layout...

1.  [workgroups2](https://github.com/pashinin/workgroups2)

This one seems to be a more comprehensive package. It allows to save and
restore workplaces and frame configurations. It seems to answer my
needs, and add some more functionality that I didn't think about at
first.

But it requires some more research and exprimintation before I can tell
if it's what I was looking for, and if it is something I can see myself
working with.

Do I want to give it a try now...? think I should, if I'm already at
that.

</div>

</div>

<div id="outline-container-orgheadline69" class="outline-3">

### Running several instances of Emacs {#orgheadline69}

<div id="text-orgheadline69" class="outline-text-3">

This should be a follow up on the "How do I change windows layout" post.
I actually want to not only switch between different layouts, but also
have different look\\theme for different windows\\documents\\layouts.

</div>

</div>

</div>

<div id="outline-container-orgheadline74" class="outline-2">

Prodissues {#orgheadline74}
----------

<div id="text-orgheadline74" class="outline-text-2">

</div>

<div id="outline-container-orgheadline71" class="outline-3">

### Adding a tag cloud {#orgheadline71}

<div id="text-orgheadline71" class="outline-text-3">

-   There's a plugin for that
-   [Here's a post about how to use the
    plugin](http://www.stevenmaude.co.uk/posts/restoring-a-tag-cloud-dispersed-by-pelican-360)

</div>

</div>

<div id="outline-container-orgheadline72" class="outline-3">

### Add inline footnotes {#orgheadline72}

<div id="text-orgheadline72" class="outline-text-3">

Yesterday I got a feedback from a friend who read [this
post](http://prodissues.com/2015/11/developer_for_a_day.html). Her
feedback was that she would have liked to be able to read the footnotes
inline, instead of having to scroll all the way down the article. That's
a good feedback, and I want to think of ways to adderss it. One way will
be to add a tooltip to the footnote reference.

</div>

<div id="outline-container-orgheadline73" class="outline-4">

#### Reference {#orgheadline73}

<div id="text-orgheadline73" class="outline-text-4">

-   [Tooltips using
    jQuery](http://syeong.jcsg.com/2012/07/07/footnote-tooltips/) - -
    this article describes the use of only tooltips, not together
    with footnotes.
-   [Footnote Tooltips using
    jQuery](http://syeong.jcsg.com/2012/07/07/footnote-tooltips/)

</div>

</div>

</div>

</div>

<div id="outline-container-orgheadline77" class="outline-2">

Wordpress {#orgheadline77}
---------

<div id="text-orgheadline77" class="outline-text-2">

</div>

<div id="outline-container-orgheadline75" class="outline-3">

### Updating wordpress - checklist {#orgheadline75}

</div>

<div id="outline-container-orgheadline76" class="outline-3">

### Importing comments from disqus {#orgheadline76}

</div>

</div>

<div id="outline-container-orgheadline90" class="outline-2">

Code {#orgheadline90}
----

<div id="text-orgheadline90" class="outline-text-2">

</div>

<div id="outline-container-orgheadline78" class="outline-3">

### Parsing emails in Python {#orgheadline78}

<div id="text-orgheadline78" class="outline-text-3">

I have an idea for an app (I'll just say it has something to do with
food and personalization...), and want to validate the problem, the
assumptions that I have, and the solution that I have in mind. New
product development 101.

Thinking of the MVP of the MVP, I want to collect some data about my own
patterns. I want to get the history of my food orders, and the best
place to look for this information is in Gmail. That's where all the
confirmation emails live.

I want to create a Python script that goes through the relevan emails,
and fetch the information I'm looking for. Part of the problem -
accessing the history of emails - is already solved, since I have all my
emails on my local machine, stored in an `/Maildir` folder (another good
reason, in retrospec, to use mu4e.)

Before parsing emails, I need to understend the ins-and-outs of python
and email management.

</div>

<div id="outline-container-orgheadline79" class="outline-4">

#### Sending email {#orgheadline79}

<div id="text-orgheadline79" class="outline-text-4">

<div class="org-src-container">

``` {.src .src-sh}
$ python3
Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 23 2015, 02:52:03) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.

>>> import smtplib
>>> smtpObj = smtplib.SMTP_SSL('smtp.example.com', 465)
>>> smtpObj.ehlo()
(250, b'mx.example.com at your service, [216.172.148.131]\nSIZE 35882577  
n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nCHUNKING')
>>> smtpObj.login('bob@example.com', ' MY_SECRET_PASSWORD')
(235, b'2.7.0 Accepted')
>>> smtpObj.sendmail('bob@example.com', 'alice@example.com', 'Subject: So
long.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob')
{}
>>> smtpObj.quit()
(221, b'2.0.0 closing connection ko10sm23097611pbd.52 - gsmtp')
```

</div>

Notes:

-   In the `sentmail` function:
    -   The body of the email defined in the third argument. It must
        start with "Subject:".
    -   The "\\n" seperates between the subject and the body of
        the email.

</div>

</div>

<div id="outline-container-orgheadline82" class="outline-4">

#### IMAP {#orgheadline82}

<div id="text-orgheadline82" class="outline-text-4">

</div>

-   [](){#orgheadline80}Install imapclient and pyzmail
    <div id="text-orgheadline80" class="outline-text-5">

    Finding and retriving emails is easier using these two modules.
    Here's how to install them:

    <div class="org-src-container">

    ``` {.src .src-sh}
    ~ $ python3 -m pip install imapclient
    ~ $ python3 -m pip install pyzmail
    ```

    </div>

    </div>

-   [](){#orgheadline81}

</div>

<div id="outline-container-orgheadline83" class="outline-4">

#### Reference {#orgheadline83}

<div id="text-orgheadline83" class="outline-text-4">

-   [Parsing email using Python part 1 of 2 : The
    Header](http://blog.magiksys.net/parsing-email-using-python-header)
-   

</div>

</div>

</div>

<div id="outline-container-orgheadline84" class="outline-3">

### Connecting to Elasticsearch (or ELK with Python) {#orgheadline84}

</div>

<div id="outline-container-orgheadline85" class="outline-3">

### Integrating Sphere with Alfred {#orgheadline85}

<div id="text-orgheadline85" class="outline-text-3">

We have a hackathon

</div>

</div>

<div id="outline-container-orgheadline86" class="outline-3">

### Adding scheduled job in mac {#orgheadline86}

<div id="text-orgheadline86" class="outline-text-3">

I want to run the `offlineimap` every x minutes. For that I can use
either keyboard maestro or LaunchAgent. Need to decide on an approach.

</div>

</div>

<div id="outline-container-orgheadline87" class="outline-3">

### How to figure out the size of a folder from terminal {#orgheadline87}

<div id="text-orgheadline87" class="outline-text-3">

Here's a quick way to find the size of a folder, via terminal

> The command `du` "summarizes disk usage of each FILE, recursively for
> directories," e.g.,
>
> <div class="org-src-container">
>
> ``` {.src .src-sh}
> du -hs /path/to/directory
> ```
>
> </div>
>
> -   `-h` is to get the numbers "human readable", e.g. get 140M instead
>     of 143260 (size in KBytes)
> -   `-s` is for summary
>
> (otherwise you'll get not only the size of the folder but also for
> everything in the folder separately)

[source](http://askubuntu.com/a/1226) to the answer in stack-overflow.

</div>

</div>

<div id="outline-container-orgheadline88" class="outline-3">

### Writing a python script for Lorem Ipsum {#orgheadline88}

<div id="text-orgheadline88" class="outline-text-3">

I want to be able to get a Lorem Ipsum text in varying length. I think I
can write a small script to do it. I will be able to run it using
alfred, with an argument for the number of words I would like to get.

</div>

</div>

<div id="outline-container-orgheadline89" class="outline-3">

### Parsing a json file with logstash {#orgheadline89}

<div id="text-orgheadline89" class="outline-text-3">

-   I downloaded the yelp academy data and would like to throw it to
    elastic search and see what I can do with it.
-   The dataset include json files with all the information within it as
    json objects.
-   I thought I could use the elasticsearch bulk upload api, like this:

<div class="org-src-container">

``` {.src .src-html}
curl -XPOST 'localhost:9200/bank/account/_bulk?pretty' --data-binary "@accounts.json"
```

</div>

But it didn't work. I googled the error that I got:

<div class="org-src-container">

``` {.src .src-html}
_dataset_business.json"
{
  "error" : {
    "root_cause" : [ {
      "type" : "illegal_argument_exception",
      "reason" : "Malformed action/metadata line [1], expected START_OBJECT or END_OBJECT but found [VALUE_STRING]"
    } ],
    "type" : "illegal_argument_exception",
    "reason" : "Malformed action/metadata line [1], expected START_OBJECT or END_OBJECT but found [VALUE_STRING]"
  },
  "status" : 400
}
```

</div>

and found that elasticsearch doesn't take this input as is. It has an
"awekward" format that it can work with, and require an `\n` at the end
of every json object.

I'm not sure I want to start parsing the json file and append `\n` to
the end of each json object. Instead, it might be a good opportunity to
try working with logstash. I'm sure it has a json plugin that takes json
file as an input, format it and send it into elasticsearch.

<http://stackoverflow.com/questions/22941739/using-json-with-logstash>

In the [logstash
documentation](https://www.elastic.co/guide/en/logstash/current/plugins-filters-json.html)
I see that I should use the json filter, and one of the required fields
is `source`. I'm not sure what this `source` field means, but keep its
value to `"message"`, following the example in the documentation.

Chacking my logstash configuration seems to be ok:

<div class="org-src-container">

``` {.src .src-sh}
~/dev/elk/logstash-2.2.2 $ bin/logstash -f yelp-json.conf --configtest
Configuration OK
```

</div>

Running logstash on my config file doesn't work though. Here's my
template file:

Nothing happens. No json is parsed. I'm spending an hour trying to
understand what I'm doing wrong, and eventually realize that its
something to do with the timestamp. I have to let logstash know that it
should start monitoring the file from the beggining, and not look for
only new entries (think it looks for entries from the last 24 hours by
default).

Ok, it finally works. As I've suspected, it was the time related
configuration. Here's my logstash config file:

<div class="org-src-container">

``` {.src .src-js}
input {
  file {
    sincedb_path => "/dev/null"
    type => "json"
    path => "/Users/ygilad/Downloads/yelp_dataset/test.json"
    start_position => beginning 
    ignore_older => 0

  }
}
filter{
    json{
        source => "message"
    }
}
output {
    elasticsearch {
                  index => "test_business"
                }
    stdout{}
}
```

</div>

The json file I would like to parse has only json objects in it, there's
no field that include the desired object. How do I point the filter to
the root of every json object?

Is it possible that I'm just too impatient, and that the configuration I
had in place worked all this time...?

I found this repository

<https://github.com/ashwintumma23/YelpBusinessDataToElasticSearch>

</div>

</div>

</div>

<div id="outline-container-orgheadline106" class="outline-2">

Work {#orgheadline106}
----

<div id="text-orgheadline106" class="outline-text-2">

</div>

<div id="outline-container-orgheadline95" class="outline-3">

### Elastic Search is amazing {#orgheadline95}

<div id="text-orgheadline95" class="outline-text-3">

</div>

<div id="outline-container-orgheadline91" class="outline-4">

#### Fraking {#orgheadline91}

<div id="text-orgheadline91" class="outline-text-4">

Few years ago, gas prices went beserk, to well over 150\$ a barrle. It
seemed as if oil will be over in just a few years. Might be good news
for some, but that's not the argument I'm trying to get at.

Anyway, just as it seemed that we are forced into a oil-less economy,
and started to think of sustainable energy resources, fraking started to
cought out steam as a way to access deep layers of pockets of gas and
oil. Suddenly oil resovoure quadrupled(?)

Again, I'm not an anti inviormentalist, so get of my back. What I'm
trying to get at is that Elastic Search is like fraking, just without
all the bad things that comes with it. Let me share with you how ES
feels like from a product point of view.

</div>

</div>

<div id="outline-container-orgheadline92" class="outline-4">

#### It took us almost a month to drill a report {#orgheadline92}

</div>

<div id="outline-container-orgheadline93" class="outline-4">

#### It took us a year to create a pool of content, and it's very limited. {#orgheadline93}

</div>

<div id="outline-container-orgheadline94" class="outline-4">

#### Elastic search brings all though resources to the ground level {#orgheadline94}

<div id="text-orgheadline94" class="outline-text-4">

Now, with easy to use interface, even non-technocal people can dig the
data and play with it. Suddenly we have milions of documents at the tip
of our finger, and I can search for documents in with any filter I'm
interested in, just like I can do with Google, only that I know that I
will get content in return.

<div class="org-src-container">

``` {.src .src-js}
{
  "size": 75,
  "query": {
    "filtered": {
      "query": {
        "range": {
          "Leiki.Metallica": {
            "gte": 0.5
          }
        }
      },
      "filter": {
        "term": {
          "langId": "en"
        }
      }
    }
  }
}
```

</div>

</div>

</div>

</div>

<div id="outline-container-orgheadline104" class="outline-3">

### Getting Feedback from users and customers {#orgheadline104}

<div id="text-orgheadline104" class="outline-text-3">

</div>

<div id="outline-container-orgheadline96" class="outline-4">

#### Intro {#orgheadline96}

<div id="text-orgheadline96" class="outline-text-4">

A friend of mine asked me the other day how do we collect feedback from
clienct, and how do we incorporate this feedback in our product roadmap.
My immediate response was that we do collect feedback. This feedback
includes not only meetings with clients, but mainly ....

But my answer got me thinking. Do we really don't collect feedback? are
we really driven only by a vision, thinking that we have all the
answers, and only building something with the hope that everyone will
understand it at the end of the day? and when I thought about it deeper,
the answer become No. Absolutly not.

</div>

</div>

<div id="outline-container-orgheadline97" class="outline-4">

#### Feedback *is* part of our process, even if we don't think of it as such {#orgheadline97}

<div id="text-orgheadline97" class="outline-text-4">

A feedback loop is essential to everything I do, whether it's through
direct partners' feedback, user testings, a\\b testing or data analysis.
Here are just few examples for the type of feedback we collected, what
we learned from it, and how it influenced our product.

</div>

</div>

<div id="outline-container-orgheadline102" class="outline-4">

#### Examples {#orgheadline102}

<div id="text-orgheadline102" class="outline-text-4">

</div>

-   [](){#orgheadline98}Direct to consumers first
    <div id="text-orgheadline98" class="outline-text-5">

    We started with direct to consumer products, such as a Firefox and
    chrome extensions. While the initial UI\\UX were driven by our
    experience working with publishers, we quickly revised it after
    gathering data from user feedback that was collected through user
    testing, engagement data (mainly google analytics) and a\\b testing.

    The feedback we gathered showed us a mixed picture. On the one hand,
    we satisfied a (small) segment of the users we saw. On the other
    hand, data showed that our building a d2c from scratch will not
    be sustainable. Our cost per user was way over the LTV.

    </div>

-   [](){#orgheadline99}NTDs
    <div id="text-orgheadline99" class="outline-text-5">

    That led us to two main decisions. 1) We should build our
    distribution first and a destination second and 2) everything we
    build should be reusable (i.e. API driven). With that decision, we
    had to first chose the types of partners that will see the value in
    what we're building. After numerous meetings with different partners
    that have different goals, we selected partners who care mostly
    about engagement and audience growth (rather than
    pure monetization). Our initial partners were companies, usually
    technology driven, that don't produce their own content, but want to
    use content to drive engagement and retention.

    Working with those partners, we learned about the KPIs they're
    interested in, and capabilities they would like to have. For
    example, one partner wanted to create an on-boarding experience to a
    content hub they were planning to build inside their app. They
    wanted to leverage our platform to power the content, but also to
    allow users to control the sites and categories of content they
    being recommended with. This request led us to expand our platform
    and expose a set of APIs that enable this functionality. Today,
    those APIs play an important role in our story.

    </div>

-   [](){#orgheadline100}Back to publishers
    <div id="text-orgheadline100" class="outline-text-5">

    As we've started to scale our pilot with partners, we found that our
    vision and the platform we've built aligns well also with a certain
    segment of publishers - small, "high brow" publishers that produce
    premium content for niche audience. Meetings and brainstorming with
    such partners, we learned that taking an API route isn't practical,
    because they usually don't have the technical capabilities to
    integrate with our platform through an API. That led us to work on a
    JS based solution, with the goal of minimizing time to deployment,
    and the required technical skills to work with us.

    We launched that new product couple of weeks ago. You can take a
    look at [that
    article](http://firstround.com/review/slacks-first-product-manager-on-how-to-make-a-firehose-of-feedback-useful/)
    from First Round Review for an example how this product looks like
    (see the recommendation units on the sides and bottom of
    the article).

    </div>

-   [](){#orgheadline101}The hackathon as a feedback loop
    <div id="text-orgheadline101" class="outline-text-5">

    The development hub that I showed briefly yesterday, was driven by
    tons of user testings, spec reviews and demos we presented
    to partners. Last week, we conducted a dry run for that platform, in
    a hackathon we organized in our office. We invited external teams to
    hack and build with our APIs. The goal was to test how
    "self-servised" and self-explanatory the work with our platform and
    documentation is.

    You can take a look at [that blog
    post](http://prodissues.com/2015/11/developer_for_a_day.html) for my
    personal lessons. But we had another, bigger and
    surprising take-away. Most of the teams in the hackathon chose to
    use one certain API, that we made available the night before the
    hackathon, just as a through away and as an afterthought, without
    knowing how it can really be leveraged. That was a unique way to
    learn about how our partners **really** want to use our platform,
    and where we might want to grow it.

    </div>

</div>

<div id="outline-container-orgheadline103" class="outline-4">

#### Summary {#orgheadline103}

</div>

</div>

<div id="outline-container-orgheadline105" class="outline-3">

### Fearute ownership {#orgheadline105}

</div>

</div>

<div id="outline-container-orgheadline108" class="outline-2">

Omakase {#orgheadline108}
-------

<div id="text-orgheadline108" class="outline-text-2">

</div>

<div id="outline-container-orgheadline107" class="outline-3">

### From Idea to Vision and Back to an MVP {#orgheadline107}

<div id="text-orgheadline107" class="outline-text-3">

The last couple of weeks were an interesting experiment in trying to
think my idea from the vision perspective. What is the need that it's
going to serve, where does it fit in the bigger ecosystem, what's the
bigger vision - a stand-alone app or a bigger platform, what's the
buiseness model, who might be good partners, exit strategy and all those
investor like information that should find its place in a presentation.

After going through that and speaking with some friend whom advice I
highly appreciate, I'm confident there is something here. There's an
idea and there's a vision. Now I had to figure out where to start.
What's the MVP?

I thought that the next thing will be to find someone who will lead the
technical front. Most of my connections are in Israel, and one of the
advises I got was to find someone local (NYC), otherwise I won't be able
to have like 3 hours in sturbacks, cracking some pesky problem together
with my co-founder.

I also read this very good article about finding a technical co-founder,
and decided to take the advise there, and start doing the technical work
that I can do, and create some value that potential candidates can
appreciate, understand and see the value in. That might also turn out to
be a good MVP.

</div>

</div>

</div>

<div id="outline-container-orgheadline112" class="outline-2">

Workflows {#orgheadline112}
---------

<div id="text-orgheadline112" class="outline-text-2">

</div>

<div id="outline-container-orgheadline109" class="outline-3">

### Process mail {#orgheadline109}

<div id="text-orgheadline109" class="outline-text-3">

This is the workflow I use for the last couple of months to process my
mail, process it to a paperless storage, and be on top of my bills.  
Ingredients:

-   2Do - a reacuring reminder to check my physical mailbox
-   Scanner pro
-   Dropbox
-   Hazel
-   DevonThink

</div>

</div>

<div id="outline-container-orgheadline110" class="outline-3">

### Remove HTML Files With Hazel {#orgheadline110}

<div id="text-orgheadline110" class="outline-text-3">

Here's a simple Hazel rule I created in order to deal with superflous
html files that are created whenever I do a file export from my
`\~/Dropbox/Notes` folder.

-   `[ ]` I need to see how I set the rule so it monitor both files
    within the folder and within sub-folder in that folder.
    -   Read through the hazel forum here: [How to get Hazel to go into
        subfolders](https://www.noodlesoft.com/forums/viewtopic.php?f=4&t=470)

</div>

</div>

<div id="outline-container-orgheadline111" class="outline-3">

### Stitch two images together {#orgheadline111}

<div id="text-orgheadline111" class="outline-text-3">

I have two screenshots I took on my iPhone. Now I want to stich them and
show them as one image, side by side.

</div>

</div>

</div>

<div id="outline-container-orgheadline128" class="outline-2">

Other {#orgheadline128}
-----

<div id="text-orgheadline128" class="outline-text-2">

</div>

<div id="outline-container-orgheadline113" class="outline-3">

### So much going on... {#orgheadline113}

<div id="text-orgheadline113" class="outline-text-3">

I wish I could start an async thread that would have gone and document
everything that's going on at the moment. So many open thread, in so
many areas of my life, that I don't find a minute to stop and document,
write or share the magnitude of learnings that I accumulate. So I'll try
to log dump at least one, which might be worthwhile for me later on, as
technical documentation and for some other readers.

</div>

<div id="outline-container-orgheadline114" class="outline-4">

#### Imapclient + Elasticsearch {#orgheadline114}

<div id="text-orgheadline114" class="outline-text-4">

I want to be able to learn about my eating habits. More specifically, I
would like to get a picture of the restaurants and dishes I'm ordering
from. My assumption is that this list is limmited, and that most of the
time I'm spending on trying to figure out what to eat is a waste,
because I end up eating the same dishes from the same places.

</div>

</div>

<div id="outline-container-orgheadline115" class="outline-4">

#### Why collecting this data? {#orgheadline115}

<div id="text-orgheadline115" class="outline-text-4">

This is a good MVP to a bigger idea that will help me (and hopefuly
others) turn the decision of 'what to eat' fun again.

</div>

</div>

<div id="outline-container-orgheadline116" class="outline-4">

</div>

</div>

<div id="outline-container-orgheadline117" class="outline-3">

### Don't Build a Dominos Pizza Company {#orgheadline117}

<div id="text-orgheadline117" class="outline-text-3">

-   Note taken on <span class="timestamp-wrapper"><span
    class="timestamp">\[2015-11-16 Mon 15:45\]</span></span>  
   started writing this

I want to follow up on my discussion with Elad today. I want to say
something about us being the wrong people at the wrong phase of the
company. But I also want to say that the company's going astray. I want
to make a metaphor to Domino's pizza. I want to say that about 20 years
ago dominoes was all about the pizza about making it the best pizza for
their customers.  
The van over the years dominoes look for other ways to make revenue.
Pizza wasn't necessarily the only thing they wanted to do in order to
grow. So, new people who join dominoes wearing to miss surly passionate
about pizza but passionate about making money. People probably join from
McDonald's and brought with them the best way to do burgers in people
join from K FC with recipes for chicken wings. So little by little those
old people who cared about pizza is where less and less relevant. Not
only that he cared about one thing but they were people of the past.

What I want to say, is that those people might be the people of the
past. It might be that Domino's is no longer at pizza place. But as a
customer I don't know the hell what Domino's is you have no identity and
it's not here to stay.

</div>

<div id="outline-container-orgheadline118" class="outline-4">

#### When Domino's pizza just started {#orgheadline118}

<div id="text-orgheadline118" class="outline-text-4">

I'm sure they were all about the pizza. How to bake the best pizza, that
will take over the world

</div>

</div>

<div id="outline-container-orgheadline119" class="outline-4">

#### At some point, pizza didn't take over the world {#orgheadline119}

</div>

<div id="outline-container-orgheadline120" class="outline-4">

#### Domino's moved to another mode {#orgheadline120}

</div>

<div id="outline-container-orgheadline121" class="outline-4">

#### Bring new people, who were more adapt to the new company {#orgheadline121}

<div id="text-orgheadline121" class="outline-text-4">

But those people didn't have the initial dna of the early dominos days.
They weren't passionate about the pizza, but about the business and
about fixing this company.

</div>

</div>

<div id="outline-container-orgheadline122" class="outline-4">

#### From kfc, and macdonald {#orgheadline122}

<div id="text-orgheadline122" class="outline-text-4">

Dominos hired people "who already did it". Some from KFC, some from
macdonald. The early employees of dominos now were part of the past.
They were naive, and didn't "grow" with the business. Sell only pizza is
so 60s.

</div>

</div>

</div>

<div id="outline-container-orgheadline123" class="outline-3">

### Webarchive {#orgheadline123}

<div id="text-orgheadline123" class="outline-text-3">

Just a reminder about this tool.

Many times I find a link that seemed to be dead. I sigh disappointed and
look for a new resource. Sometimes I recall this amazing site, tha

</div>

</div>

<div id="outline-container-orgheadline124" class="outline-3">

### It's not about you. It's about the topic. {#orgheadline124}

<div id="text-orgheadline124" class="outline-text-3">

Recently I spend more and more time in social networks other than the
ones like Twitter and FB, though I rarely used FB. But my point is that
my attention shifted to other channels.

The results of that narcissism:

-   I started to use Reddit more, because I was interested in the topic.
-   I found it more and more engaging. I liked it, because it didn't
    feel like a waste of time. It's knowledge about the things I'm
    interested in. (Emacs, product management, writing).
-   Engagment led to participation.
-   But then the equation skewed. Instead of logging it and read the new
    posts, for days I would open Reddit and scroll to find
    my submissions. How many upvotes were added? Any new comments? I
    suddenly noticed that I scroll past days of discussion, just to
    selfishly check the status of **my** posts.
-   Than, few long days went by without me posting anything.
    Stat flattens. And suddenly I have less interest opening the app. No
    point, no one commented on what I said.

</div>

<div id="outline-container-orgheadline125" class="outline-4">

#### So what's the point I'm trying to make? {#orgheadline125}

<div id="text-orgheadline125" class="outline-text-4">

Is it the obsession with self centric attention? Is it the tension
between narcissism and essence

</div>

</div>

</div>

<div id="outline-container-orgheadline126" class="outline-3">

### Mechanical Keybords {#orgheadline126}

</div>

<div id="outline-container-orgheadline127" class="outline-3">

### POST - how to make yourself look dumb {#orgheadline127}

<div id="text-orgheadline127" class="outline-text-3">

So here's a very effective tip to how to expedite the first impression
your communicating, down hill.

Earlier today I met with several executives from a company that do
mobile development. The goal of the meeting was to brainstorm ideas and
ways we can collaborate.

After some chitchat we started the meeting. Before any of the
participants introduced themselves, let alone giving some context to the
meeting, one of the executive said something like:

"So let me guess, your challenge in mobile is that you didn't figure out
the creative to drive the monetization your partners are looking to
drive"

My respond was simple, yet somewhat blunt:  
"Wrong guess. Do you want to try again, or do you prefer I give some
background and context?"

From that moment on, I couldn't make myself listens and take things that
came out from that guy's mouth seriously. Instinctively I shut my ears
to his comments, filtering them and waiting for him to go silent and let
other people talk.

The takeaway:  
What a bad strategy it is to come to a discussion with prior conviction,
and blah your assumption on the table, before hearing something or
looking for clues from the other side. The stacks are too high. It's
like sitting in the blackjack table and asking "hit me" before being
felt for the first card.

But this goes well beyond discussions. How many times did you see
managers falling into this trap? Starting a new role with decisions and
actions, before taking the time to learn and listen.  
\[add my essay to business school?\]

</div>

</div>

</div>

<div id="footnotes">

Footnotes: {#footnotes .footnotes}
----------

<div id="text-footnotes">

<div class="footdef">

^[1](#fnr.1){#fn.1 .footnum}^

<div class="footpara">

I'm borrowing this concept from Mickey Petersen, in his book [Mastering
Emacs](https://www.masteringemacs.org)

</div>

</div>

<div class="footdef">

^[2](#fnr.2){#fn.2 .footnum}^

<div class="footpara">

Just make sure you don't stepping inside of another decleration.

</div>

</div>

<div class="footdef">

^[3](#fnr.3){#fn.3 .footnum}^

<div class="footpara">

The way [EmacsWiki](http://www.emacswiki.org/emacs/DiredExtra#Dired_X)
suggests to enable it didn't work for me, because it requires to use
dired before using dired-x.

</div>

</div>

<div class="footdef">

^[4](#fnr.4){#fn.4 .footnum}^

<div class="footpara">

I still follow a tip that I've learned from my C professor - always
insert pairs - so I never have to worry about finding which parentheses
I forgot to close.

</div>

</div>

<div class="footdef">

^[5](#fnr.5){#fn.5 .footnum}^

<div class="footpara">

Note to self - is it a true assumption that I can tell from a variable
name whether it can hold a list of only a single value?

</div>

</div>

</div>

</div>

</div>
