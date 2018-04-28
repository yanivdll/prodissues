Title: A Recipe To Work-In-Progress Documents
Date: 2015-09-12 01:58
Author: yaniv
Category: code
Tags: Automation, Hazel, python
Slug: a-recipe-to-work-in-progress-documents
Status: published

I recently [stopped using
Evernote](http://prodissues.com/2015/06/why-i-decided-to-move-away-from-evernote.html)
and started to manage my notes exclusively in Dropbox. My configuration
revolves around a `Notes` folder. I use
[nvAlt](http://brettterpstra.com/projects/nvalt/) to browse through the
notes in that folder and add new ones. If I want to do more than just a
scribble, I use the `command-e` key binding in nvAlt to open the
document in [MultiMarkdown Composer](http://multimarkdown.com/).

Storing all my notes in one folder has a major limitation, though. As
notes accumulate, looking for a specific note becomes impossible. This
is actually one of the main reasons to my departure from Evernote. To
avoid this problem, I set [Hazel](http://www.noodlesoft.com/hazel.php)
to monitor my `Notes` folder and move everything that wasn't modified in
the last 30 days to a designated archive folder. Archived notes don't
show in nvAlt, yet easily accessible through Finder.

Now that I have a home to my notes, I would like to add some logic to
streamline my writing workflow. To begin with, I would like to aggregate
documents I'm working on, and are in other folders, to my main notes'
repository.

For example, I'm currently writing a readme file for one of my git
repositories. This repo lives within its own folder, where the readme
file resides as well. Keeping this file out of my `Notes` folder means
that it's a hassle to go back and open it when needed. It also means
that I can't work on it when I'm on my iPhone ^[1](#fn.1){#fnr.1
.footref}^.

So, what I needed was a way to mark a document, and have it magically
show up in my `Notes` folder, hence available in nvAlt. Following is the
recipe I came up with to address this need.

Let's start with the ingredients:

-   Finder
-   Hazel
-   Python

And here's how to mix these components together:

1.  Open Finder and tag `wip` the document I want to work on and make
    available in
    nvAlt.![tag\_wip.png](http://media.prodissues.com/images/2015/09/tag_wip.png)
2.  Configure a Hazel rule that monitors my home folder, looking for
    files containing the `wip` tag ^[2](#fn.2){#fnr.2 .footref}^.
    ![hazel\_3.png](http://media.prodissues.com/images/2015/09/hazel_3.png)
3.  Create a python script that takes a file's path as an input and
    place a symbolic link to it in my `Notes` folder.



``` python

#! /usr/local/bin/python3

import os, sys, shutil
import logging

# Configuring logging to be written into a file in the system's log folder
logging.disable(logging.CRITICAL)
logging.basicConfig(filename='/Users/ygilad/Library/Logs/Python/myPythonLogs.log', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

def moveFileToNote(filePath):
    # Set the link name to the original file.
    # Path to the original file is included for two reasons
    # 1) Avoid naming conflicts and
    # 2) remind myself where this file came from
    fileName = 'link' + filePath.replace('/','_').lower()
    logging.debug('Filename: ' + fileName)

    # Make sure that the input is a file and not a folder
    if len(fileName) > 0:
        try:
            # Add the link to my central note repository
            os.symlink(filePath , '/Users/ygilad/Dropbox/Notes/link-'+ fileName)
            logging.debug('Created a file link')
        except FileExistsError:
            logging.debug('File already exists at the target folder')
    else:
        logging.debug('Input is not a file')

# Accept the path coming from Hazel
hazelLocalFile = sys.argv[1]
logging.debug(hazelLocalFile)

# The body of the script
moveFileToNote(hazelLocalFile)

```

There is one drawback I wasn't able to solve - nvAlt doesn't show the
content of the link. All it *does* show is the path of the original
document.![nvAlt\_and\_linked\_files.png](http://media.prodissues.com/images/2015/09/nvAlt_and_linked_files.png)

While I can't edit the file directly in nvAlt, I can still do it in
MultiMarkdown Composer or
[Editorial](http://omz-software.com/editorial/) on my iPhone.


[^1]:I keep git repositories in a local folder out of Dropbox reach, because
I heard that [you shouldn't mix the two
together](http://scripting.com/2014/01/24/githubAndDropboxDoNotPlayWellTogether.html).



[^2]: I found that creating a rule that monitors a folder and its sub-folders
is a bit tricky, but eventually learned how to do it thanks to [this
post](http://www.noodlesoft.com/forums/viewtopic.php?f=4&t=470).