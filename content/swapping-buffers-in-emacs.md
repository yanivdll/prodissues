title: Swapping Buffers in Emacs
date: 2015-11-07 22:39:00
status: 
process: @post
tags: emacs
synonym: plain text
---

It took me awhile to find a way to swap the position of two buffers in emacs. Yes, there is a description in [emacs wiki](<http://www.emacswiki.org/emacs/SwitchingBuffers>), and the code bellow is actually taken from there, but it's not that easy to find through the tons of irrelevant information arround it.

So if you're looking to simply get the right buffer show on the right, and vice versa, here's what you should add to your init file:

```elisp
    (defun transpose-buffers (arg)
      "Transpose the buffers shown in two windows."
      (interactive "p")
      (let ((selector (if (>= arg 0) 'next-window 'previous-window)))
        (while (/= arg 0)
          (let ((this-win (window-buffer))
                (next-win (window-buffer (funcall selector))))
            (set-window-buffer (selected-window) next-win)
            (set-window-buffer (funcall selector) this-win)
            (select-window (funcall selector)))
          (setq arg (if (plusp arg) (1- arg) (1+ arg))))))
```
          
I have no idea what this code means[^1], but it does what it supposed to. I also didn't create a keybinding for it, but you can I you want. Here's how to bind it to, say, `f8`:

```elisp
    (global-set-key [f8] 'transpose-buffers)
```





[^1]: Learning elisp is on my todo list
