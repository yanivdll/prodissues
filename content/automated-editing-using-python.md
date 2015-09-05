---
title: Find Repetitive Words Using Python
date: 2015-09-02 02:21 UTC
tags: python, writing
category: Code 
---

Read this question from [stackoverflow](http://stackoverflow.com/questions/2823016/regular-expression-for-consecutive-duplicate-words): 

> Paris in the  
> the spring. Not that  
> that is related.
> 
> Why are you laughing? Are my my regular expressions THAT bad??

Have you notice the repetitions? chances are you haven't. The eye sees what the eye wants to see, and it'll take away any obstacle to let your brain comprehend. I too often catch myself writing the same word twice. The problem is that when I do, it's usually too late. The email was sent or post got  published. 

To make sure I find those repetitions in time, I wrote a simple Python script that removes superfluous spaces and highlight words' duplications, using [CriticMarkup](http://criticmarkup.com). I run this script as soon as I finish writing. It works much better than my eyes in finding those elusive duplications.

Here's the script:

```python
#! /usr/local/bin/python3
# removeRepeatWords.py - find and remove repeat words
import logging
logging.basicConfig(filename='/Users/ygilad/Library/Logs/Python/myPythonLogs.log', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.disable(logging.CRITICAL)

import pyperclip, re

text = str(pyperclip.paste())

#regex definitions for reapeated spaces
repeatSpacesRegex = re.compile(r'\b(\s)+\1+\b') 

#regex definitions for reapeated words
repeatWordsRegex = re.compile(r'\b(\w+)\b[\s\r\n]*(\1[\s\r\n])+', re.IGNORECASE|re.DOTALL)

#remove the extra spaces
repeatSpces = repeatSpacesRegex.findall(text)

if len(repeatSpces) > 1:
    text = repeatSpacesRegex.sub(r'\1', text)
    print(str(len(repeatSpces)) + ' repeat spaces were removed.')

#remove repeated words
repeatWords = repeatWordsRegex.findall(text)
logging.debug(repeatWords)

if len(repeatWords) > 0:
    text = repeatWordsRegex.sub(r'{~~\1 \2~>\1 ~~}{>>repeating words<<}', text)

pyperclip.copy(text)
```

To use it, copy the text you want to check into the clipboard. You then run the script and its output will be ready for you back in the clipboard. Just past it over the original text. Note that if the script finds repetitions it won't remove them, but mark them using CriticMarkup. If your editor supports CM, you can decide whether to accept or reject those changes. 

Running this script on the quote from stackoverflow above produces the following output:

```text
Paris in {~~the  the ~>the~~}{>>repeating words<<}spring. Not {~~that  that ~>that~~}{>>repeating words<<}is related.
 
Why are you laughing? Are {~~my  my ~>my~~}{>>repeating words<<}regular expressions THAT bad??
```
