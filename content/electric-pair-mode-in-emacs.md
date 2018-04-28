Title: Electric Pair Mode In Emacs
Date: 2016-10-02 00:00
Author: yaniv
Category: emacs
Tags: packages
Slug: electric-pair-mode-in-emacs
Status: published

So far I've used [TextExpander](https://textexpander.com) for text
snippets and, well, text expansion. One of my main uses-cases is
character pairings. For example, when I type `"` I almost always enclose
it with another `"`.

But TextExpander is lacking in several ways:

1.  Performance - it takes a friction of a second for the expansion to
    happen, but it's notable, and feels like a little hang.
2.  If I delete one part of the pair, it won't remove the other.
3.  It won't work to wrap text. If I typed something, and then want to
    wrap it with brackets, for example, I can't select the text and type
    the bracket character.

In addition to the above technical shortcomings, I don't plan to keep
using TextExpander in the long run. The recent [move into subscription
based](http://www.macworld.com/article/3052440/os-x/smile-updates-textexpander-and-switches-to-subscriptions.html)
pricing, isn't something I'm interested in. I mean, paying subscription
to text snippets...?

Anyway, Emacs comes with an electric-pair-mode, which enables smart
pairing. I turned it on, but out of the box it's configured to work
mainly with programming major modes. I need it also in other text based
modes, such as org, markdown and simple text. For example, in org I use
`~` for inline code snippets, and `~` isn't paired by default. Same goes
with `"`.

Luckily, defining more pairs is easy, through modifying the
electric-pair-pairs variable.

Here's my configuration for this mode:


```lisp
(electric-pair-mode 1)
(setq electric-pair-pairs '(
                            (?\ . ?\)
                            (?\ . ?\)
                            (?\( . ?\))
                            (?\{ . ?\})
                            ))
```

I'll add more pairs as I encounter them. Also, I'll need to learn how to
add pairs for specific major modes.
