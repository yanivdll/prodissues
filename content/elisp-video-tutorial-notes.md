Title: Elisp Video Tutorial - Notes
Date: 2016-10-18 22:12
Author: yaniv
Category: emacs
Tags: elisp, tutorial
Slug: elisp-video-tutorial-notes
Status: published

I've just finished watching [Daniel Gopar's](http://www.pygopar.com/)
elisp [video tutorial](https://www.youtube.com/watch?list=PL3kg5TcOuFlpyqiZspzlkk6Ro66nQdESz&params=OAFIAVgB&v=CH0RUrO_oww&mode=NORMAL&app=desktop). So far there are 4 parts to the tutorial, and based on [this thread](https://www.reddit.com/r/emacs/comments/5542rm/made_some_elisp_videos/?) on Reddit, there are more to come.

After watching the guide I don't feel more proficient in elisp, yet less timid running `evals` and more courageous tinkering with my [config](https://github.com/yanivdll/.emacs.d/blob/master/config.org) file.

Following is a short summary of the code exercises and shortcuts I
logged while watching.

## Part 1 - Intro

[Link to episode 1](https://www.youtube.com/watch?list=PL3kg5TcOuFlpyqiZspzlkk6Ro66nQdESz&params=OAFIAVgB&v=CH0RUrO_oww&mode=NORMAL&app=desktop)

REPL - read-eval-print-loop

Define functions:

``` lisp
(defun add-num (a b) (+ a b))
```


Define a test:


``` lisp
(require 'ert)
(ert-deftest add-num-pos ()
         (should
         (equal (add-num 10 10) 20)))
```


To run the test that I've just created:
`M-x ert-run-tests-interactively`

Choose the test I would like to run (in this case "pos-add-num")

## Part 2 - Create A Simple Function And A Test Of That Function 

[Link to episode 2](https://www.youtube.com/watch?list=PL3kg5TcOuFlpyqiZspzlkk6Ro66nQdESz&params=OAFIAVgB&v=CH0RUrO_oww&mode=NORMAL&app=desktop)

`setq` to set variables and lists `(setq my-list '(1 2 3))`

`add-to-list` to add element `(add-to-list 'my-list 4)`

Another way to add to list, but this time to a copy of the list:
`(cons 5 my-list)` - this will return (5 1 2 3 4) But when inquiring
my-list, we will get (1 2 3 4)

`car` returns the first element in every list `(car my-list)` -&gt; 1

`cdr` returns everything from a list, after the first element
`(crd my-list)` -&gt; (2 3 4)

`nth` return a certain element in the list `(nth 4 my-list)` -&gt; 3

`member` check for a certain value in a list, and return the elements in
that list from that value on `(member 3 my-list)` -&gt; (3 4)
`(member 7 my-list)` -&gt; nil

## Part 3 - Looping And Local Variables

[Link to episode 3](https://www.youtube.com/watch?v=VqCSbDqHziM&list=PL3kg5TcOuFlpyqiZspzlkk6Ro66nQdESz&index=3)
</p>

Use the **scratch** buffer, so I can write in multiple lines

`C-x C-e` to evaluate code. Point needs to be at the end of the code in
order to get evaluated.

Looping through variables:

`let` to create a local variable

`when` and `if` - what they suppose to do...

If there is more than one statement in the `if` statement, need to use
to wrap those lines with `progn`. There is no such limitation in the
`else` statement.

## Part 4 - Interactive Functions

[Link to episode 4](https://www.youtube.com/watch?v=KwBRpS9Bs4U&index=4&list=PL3kg5TcOuFlpyqiZspzlkk6Ro66nQdESz)

Created a function to count words, plus the test for it.



``` lisp
(defun cheap-count-words()
  (interactive)
  (let ((words 0))
    (save-excursion
      (goto-char (point-min))
    (while (forward-word)
      (setq words (1+ words)) ))
    (message (format "Words in Buffer: %s" words))words))



;; Tests
(require 'ert)

(ert-deftest count-words-test ()
  (get-buffer-create "*test*")
  (with-current-buffer "*test*"
    (erase-buffer)
    (insert "Hello world")
    (should (=(cheap-count-words) 2)))
  (kill-buffer "*test*"))
```