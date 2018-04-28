Title: Get The Current File's Path in Emacs
Date: 2016-01-04 00:00
Author: yaniv
Category: emacs
Tags: code, emacs
Slug: get-the-current-files-path-in-emacs
Status: published

Here's a small function I borrowed from [this
question](http://stackoverflow.com/questions/3669511/the-function-to-show-current-files-full-path-in-mini-buffer)
on stack-overflow. It returns the full path of the file I currently edit
in the buffer:

```lisp
(defun show-file-name ()
  "Show the full path file name in the minibuffer."
  (interactive)
  (message (buffer-file-name))
  (kill-new (file-truename buffer-file-name))
)
(global-set-key "\C-cz" 'show-file-name)
```


You'll note that this function is bind to `C-c z`. So when typing it,
you should see the path showing in the minibuffer. As a bonus, it stores
the path in the kill ring, so `C-y` (`CMD-v` works as well on my mac)
will paste the value.
