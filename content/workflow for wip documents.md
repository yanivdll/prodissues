title: A Recipe To Work-In-Progress Documents
date: 2015-07-08 14:07:00
process: @post
tags: Python, Hazel, Automation
synonym: plain text
---

I recently [stopped using Evernote](http://prodissues.com/2015/06/why-i-decided-to-move-away-from-evernote.html) and started to manage my notes exclusively in Dropbox. My configuration revolves around a `Notes` folder, and I use nvAlt to browse through the notes there and add new ones. If I want to do more than just a scribble, I use the `command-e` key binding in nvAlt to open the document in [MultiMarkdown Composer](http://multimarkdown.com). 

Storing all my notes in one folder has a major limitation, though. As notes accumulate, it becomes increasingly hard to find the one note I'm looking for. This is actually one of the main reasons to my departure from Evernote. To avoid this problem, I set [Hazel](www.noodlesoft.com/hazel.php) to monitor the `Notes` folder and move everything that wasn't modified in the last 30 days to a designated archive folder. Archived notes don't show in nvAlt, yet easily accessible through Finder.

Now that I have a home to my notes, I would like to add some logic to streamline my writing workflow. To begin with, I would like to aggregate documents I'm working on, and are in other folders to my main notes repository. 

For example, I'm currently writing a readme file for one of my git repositories. This repo lives in its own folder, where the readme file resides as well. Keeping this file out of my `Notes` folder means that it's a hassle to go back and open it when needed. It also means that I can't work on it when I'm on my iPhone[^iphone]. 

So, what I wanted was a way to mark documents I'm working on, and have them magically show up in my `Notes` folder, hence available in nvAlt. Following is the recipe I came up with to address this need.

Let's start with the ingredients:

* Finder
* Hazel
* Python

And here's how to mix these components together:

1. Open Finder and tag `wip` the document I want to work on and make available in nvAlt.![Add tag:wip](http://media.prodissues.com/images/2015/09/tag_wip.png "Adding a wip tag to the file I would like to have available in my Notes folder")
2. Create a Hazel rule that monitors my home folder, looking for files containing the `wip` tag[^hazel_folders]. ![Hazel rule](http://media.prodissues.com/images/2015/09/hazel_3.png "Monitor files with tag:wip")
3. Create the python script that takes a file's path as an input and place a symbolic link to it in my `Notes` folder.

```python
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

There is one drawback I wasn't able to solve - nvAlt doesn't show the content of the link. All it does show is the path of the original document.![nvAlt with links](http://media.prodissues.com/images/2015/09/nvAlt_and_linked_files.png "nvAlt doesn't play nice with symbolic links")

While I can't edit the file directly in nvAlt, I can still do it in MultiMarkdown Composer or [Editorial](http://omz-software.com/editorial/) on my iPhone.



[^iphone]: I keep git repositories in a local folder out of Dropbox reach, because I heard that [you shouldn't mix the two together](http://scripting.com/2014/01/24/githubAndDropboxDoNotPlayWellTogether.html).

[^hazel_folders]: I found that creating a rule that monitors a folder and its sub-folders is a bit tricky, but eventually found the way to do it thanks to [this post](http://www.noodlesoft.com/forums/viewtopic.php?f=4&t=470).
