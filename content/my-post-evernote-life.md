Title: My Post-Evernote Life
Date: 2015-12-31 05:00
Author: yaniv
Category: geeking, Uncategorized
Tags: evernote, workflows
Slug: my-post-evernote-life
Status: published


# Table of Contents

1. [Note taking](#note-taking)
2. [Bookmarks and references](#bookmarks)
3. [Scans](#scans)
4. [Passwords and secure notes](#passwords)
5. [Image annotations](#annotations)
6. [List and Todos](#lists)
7. [Images](#images)
8. [Journal/diary](#journal)


Few months ago I wrote about my decision to [move away from
Evernote](http://prodissues.com/2015/06/why-i-decided-to-move-away-from-evernote.html).
Recently, few readers^[1](#fn.1){#fnr.1 .footref}^ emailed me to ask
whether I actually stooped using Evernote, and if I did, what's my
alternative solution.

<!--more-->

So yes, I've stopped using Evernote (although I *do* use some of its
satellite apps, as you'll note bellow). I still have it installed,
because I didn't migrated my notes somewhere else, and therefore, every
now and then I'll have to pull out a note from it, usually a password or
a certain id number.

And yes, I have an alternative. But rather than one tool that inherited
everything I use Evernote for, I use a set of specialized apps and
services, each dedicated to a certain function or use-case.

I've tried to summaries those tools bellow. Drop a comment or[email
me](mailto:yanivdll@gmail.com) for other use-cases, or if you want to
suggest other apps. Let's start:

 <a name="note-taking"></a>
## Note taking

-   I store all my notes in plain text based files. If I've learned
    anything from my experience with Evernote is that never again will I
    keep my notes and documents in a proprietary format. Everything I
    produce must be agnostic to the tool I create it with.
-   All of my notes are stored in a Dropbox folder (\~/Dropbox/Notes).
    That way I can access them from anywhere.
-   I use several apps to create, edit, search and manage my notes,
    depending on the platform I'm on:
    -   iOS
        -   I start almost every new notes in
            [Drafts](http://agiletortoise.com/drafts/) because it opens
            quickly, ready to accept my input. It also serves as a
            terminal, from which my notes depart to their
            final destination. Those destinations might be an email,
            calendar event, document or a blog post. There are many
            more, though. Take a look at [Drafts' action
            directory](http://drafts4-actions.agiletortoise.com/) to get
            a sense of them.
        -   [Editorial](http://omz-software.com/editorial/) - a
            comprehensive editor for iOS. I use it to edit existing
            notes, or to elaborate on a note I've started in Drafts.
    -   Mac ^[2](#fn.2){#fnr.2 .footref}^
        -   I use an app called
            [nvAlt](http://brettterpstra.com/projects/nvalt/) to manage
            those notes. I use it to search for (it has great
            searching capabilities) or start new notes.
        -   [MultiMarkdown Composer](http://multimarkdown.com/) - full
            blown multimarkdown editor (but it can be used for many more
            formats as well). When thinking about it, my workflow on mac
            resemble that on mobile - I usually start my notes in nvAlt,
            which is good for taking quick and short notes. Then, if I
            want to expand on a document, I'll open it in MMD.
        -   Google Docs - for sharing and collaborate with colleagues.
            Usually I'll write a first draft in nvAlt or MMD, and then
            export it to google docs.


<a name="bookmarks"></a>
## Bookmarks and references

-   I use [Pinboard](https://pinboard.in/u:yanivdll) as my
    bookmarks manager. It's a paid service, offering a simple, no
    fluff service. 11\$ a year and it has you covered.

<a name="scans"></a>
## Scans

-   I use a service called [FileThis](https://filethis.com/) to download
    invoices and store them in a another Dropbox folder. This service
    connects to providers, such as my bank, cable company or mobile
    provider, and download my invoices once a month. This service is
    free when connecting up to 6 providers (I've connected 4 so far).
-   I still use one of Evernote mobile apps -
    [scannable](https://evernote.com/products/scannable/) for on the
    go scans. Frankly, I love this app; it's fast, accurate and produce
    superb images. It does much better job, and much faster than, say, a
    physical scanner. It also allow me to save scan wherever I want. I
    usually either send a copy of the scans and discard the original, or
    save them to my Dropbox.

<a name="passwords"></a>
## Passwords and secure notes

-   Very simple - I use [1password](https://agilebits.com/onepassword)
    for that.

<a name="annotations"></a>
## Image annotations

Sometimes I need to take a screen-grab and add annotate it. I don't do
it often, and therefore didn't switch from Evernote's
[Skitch](https://evernote.com/skitch/). Skitch saves my annotated images
to Evernote, but I don't care about it. If I need them for future use,
I'll either upload them to Amazon S3 (where I store this site), or save
them to my Dropbox.


<a name="lists"></a>
## List and Todos

I've rarely used Evernote for reminders and todos, as it never excelled
in managing them. In addition, todos and GTD are completely different
beast, with separate workflows, and with their own set of tools. Let me
know if you're interested, and I'll expand on that in a separate post.
In essence, though, here are the main tools I use to manage my todos:

-   Apple Reminders - that's my repository for everything with a due
    date, and include no more than one atomic task. I then add reminders
    from my mac, iPad or iPhone, as well as from 3rd party apps, such as
    [Fantastical](https://flexibits.com/fantastical).
-   [Taskpaper](http://www.hogbaysoftware.com/products/taskpaper) -
    simple, yet robust, text based task manager. I use it for my
    GTD workflow. It can hold huge amount of data, and has powerful
    search capabilities. Here's a[good
    review](http://www.macdrifter.com/2014/02/the-taskpaper-rd-notebook.html)
    of that tool. Only caveat is that the app is somewhat deprecated,
    with limited to no support from the developer.

<a name="images"></a>
## Images

I used to store select images in Evernote. Kind of like a journal. I
didn't find a solution for that use-case yet. But it is also not a
priority.


<a name="journal"></a>
## Journal/diary

I used to throw journaling notes into Evernote. For example, if I
changed my mobile data plan, I would add a note, just to mark the date
of the change, for future reference. Now I have one file in my Dropbox
notes folder, to which I append entries, preceded with the date they
were entered.

I think that covers most of what I used Evernote for. Again, happy to
learn about more tools you find as good alternatives to Evernote.

[^1]: Their number is still much, much, smaller than that of the users I
converted into using Evernote over the years...

[^2]: Now, if you have the heart for it (and to be honest, I don't recommend
taking that path), I moved everything text based to
[Emacs](https://www.gnu.org/software/emacs/)... I still store all my
notes in Dropbox, but access, manage and edit them (and lots more) in
Emacs.