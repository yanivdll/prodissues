title: Combine Multiple PDF Files Into One 
date: 2015-09-28 13:58:00
process: @post
tags: python, automation
synonym: plain text
---

I often have to send pdf documents via email. When I do, I prefer to send one document that merges all those pdfs. Form a recipient point-of-view, I find it better to receive one attachment, because it's easier to manage and to keep track of. The problem is that I've yet to find an easy way to stitch together multiple pdf files. Preview supose to let you do it, but I usually can't get it to work, and when I do, the process is painful [^pain].

Recently, I came up with way to do just that, thanks to a python script I found in the ["Automate the Boring Stuff with Python"](https://automatetheboringstuff.com/chapter13/) book. This script takes a folder of documents as an input, search for all the pdf files in that folder, and combine them into one pdf file. 

However, I had to modify this script to fit my workflow better. My pdf files are all over the place, and I don't want to move them around just for the sake of merging them together. I therefore made a little tinkering to the original script, so it can take a list of files' paths as an input. Here's my modified version:

```python
#! /usr/local/bin/python3
# combinePdfsFromFiles.py - 
# Script gets a list of pdf files' paths and combine them into one file
# I use it together with keyboard maestro

import PyPDF2
import os
import sys
import logging
import pyperclip

pdfFiles = []

# Get PDF filenames from the clipboard
for filename in pyperclip.paste().split(','):
    if filename.endswith('.pdf') and filename != '':
        pdfFiles.append(filename)

pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

#Loop through all the PDF files.
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    #Loop through all the pages (except the first) and add them.
    # If first page should be discarded, change firt param of range to 1
    for pageNum in range(0, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

#TODO: add an argument that determine whether cover should be included.

#Save the resulting PDF to a file.
pdfOutput = open('/Users/ygilad/Desktop/allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
```

I created a simple keyboard maestro macro that goes along with this script and serves as an interface with it:

![KM macro](http://media.prodissues.com/images/2015/09/combine_pdfs_macro.jpg "KM macro")

Now, All I have to do is select in Finder the files I want to stitch:

![Select the files to combine](http://media.prodissues.com/images/2015/09/stich_pdf_-_select_files.png "Select files in Finder")

I can then execute the KM macro, which pass the list of files to the python script for processing.

I know this process might sound tedious, and even more painful than using Preview for that job. But that's the beauty of automation - you pay once use freely ever after.


[^pain]: To get it done with Preview, you'll have to open each of the pdfs, expose the thumbnails' sidebar, and start dragging and dropping the pages you would like to combine. If you're still interested, [here's](https://support.apple.com/en-us/HT202945) Apple's support guide. 
