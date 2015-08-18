---
title: Automated Editing Using Python
date: 2015-08-15 02:21 UTC
tags:
---
Read this:


Here's a simple script I wrote for catching repetitive to
to repetitive words. 

I trigger it after finishing to write an article, to make sure that my eyes weren't decided by repetitive words illusion.

Here's the script:

```ruby
def my_cool_method(message)
puts message
end
def my_cool_method(message)
puts message
end
def my_cool_method(message)
puts message
end
```

```python
#! /usr/local/bin/python3
# removeRepeatWords.py - find and remove repeat words

import pyperclip, re

text = str(pyperclip.paste())

#regex definitions for reapeated spaces
repeatSpacesRegex = re.compile(r'\b(\s)+\1+\b') 

#regex definitions for reapeated words
repeatRegex = re.compile(r'\b((\w+)\s+)\1\b')

#remove the extra spaces
repeatSpces = repeatSpacesRegex.findall(text)

if len(repeatSpces) > 1:
text = repeatSpacesRegex.sub(r'\1', text)
print(str(len(repeatSpces)) + ' instances of repeat spaces were removed.')

#remove repeated words
repeatWords = repeatRegex.findall(text)

if len(repeatWords) > 0:
print('Here is the list of repeated words:' + str(repeatWords))
text = repeatRegex.sub(r'\1', text)
print('Repeated words were removed from the text. Repaired text is in the clipboard.')
else:
print('Nice work. No repeat words were find.')

pyperclip.copy(text)
```

