Title: use-package's :config vs. :init
Date: 2016-10-25 10:36
Author: yaniv
Category: emacs
Tags: code, elisp
Slug: use-packages-config-vs-init
Status: published

I read [this](https://www.reddit.com/r/emacs/comments/58v6id/what_is_your_favorite_dark_theme_that_works_well/?ref=share&ref_source=link)
Reddit thread about favorite themes, and got intrigued by the [spacemacs](https://github.com/nashamri/spacemacs-theme) theme[^1].

I added that theme to my `init` file, and tried making it the default
theme. I use `use-package`, and configured the theme as follows:

``` lisp
(use-package spacemacs-theme
:ensure t
:config
(load-theme 'spacemacs-light t)
)
```


When re-evaluating my `init` file, the theme didn't load. I tried to run
only the `(load-theme 'spacemacs-light t)` line, and the theme loaded. I
changed the `:config` to `:init` in the package configuration, and it
loaded when I re-loaded emacs.

What, then, is the difference between `:init` and `:config` in
`use-package`?

The answer to that question, which I found it in this [stack-overflow
answer](http://emacs.stackexchange.com/a/10403), is that in
`use-package`, whatever defined inside the `:init` keyword, will load
whenever emacs is loading. What's in the `:config`, though, will be
executed only when the package is actually loaded (i.e lazy
loading)[^2].

Here's how my configuration for that theme looks like now:


``` lisp
(use-package spacemacs-theme
:ensure t
:init
(load-theme 'spacemacs-light t)
)
```

[^1]: I tried spacemacs before, and liked its look and feel, but didn't know I
can take it back with me to gnu emacs

[^2]: Needless to say that, going back to the `use-package` documentation, the
difference between `:init` and `:config` is clearly described…