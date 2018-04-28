Title: Should I Keep Using Pelican Or Move To Wordpress
Date: 2016-01-18 00:00
Author: yaniv
Category: blogging
Tags: pelican, Wordpress
Slug: should-i-keep-using-pelican-or-move-to-wordpress
Status: published

I'm currently using [Pelican](http://docs.getpelican.com/en/3.6.3/) to
power this site. Pelican is a static site generator (SSG) that takes
markdown files as an input and generate html pages as an output; no
database, no server-side logic; just simple, static HTML.

When I created this blog, using Wordpress or Tumblr wasn't an option,
simply because every geeky blogger I follow wrote about how much those
platforms suck, and how using SSG to run their blog were the best move
they have ever made. I chose Pelican[^1],
because of its popularity and because it is written in Python.

<!--more-->

Recently, though, I've started to question my decision. I found that I
spend more time on site administration than on writing. Tinkering with
the plumbing of the site meant that I have less time to write. And since
getting more productive with my writing is a [personal
goals](http://prodissues.com/2015/12/thinking-with-words.html), I've
started to play with the idea of switching to Wordpress.

The first thing that I've learned was that moving *from* SSG *to*
Wordpress meant swimming against the current. It isn't the cool thing to
do. Yet. As such, no one writes about it, except for Martin, who shares
in his post ["The Static Site Generator Pelican VS
WordPress"](http://ronn-bundgaard.dk/blog/the-static-site-generator-pelican-vs-wordpress/#comment-14937)[^2] many of the pains I'll be discussing here in a moment.

With that, here's is my assessment of what I like and dislike about
Pelican, and what I expect to get (or not) from Wordpress. I hope this
will help me make up my mind, and get clearer on what should be my next
steps.


## Things that I like about Pelican

-   ****The coding experience**** - I'm not a full time developer.
    Building this site helps me maintain *some* level of
    coding proficiency.
-   ****Writing in markdown**** - when writing a post, I can focus on
    the content and not on the format and styling.
-   ****No database and no server side logic**** - pages load faster,
    and my site is supposed to be more secure (since everything is
    static, there is almost no way to hack it).
-   ****Absolute control**** - the entire site is encapsulated in one
    [git repository](https://github.com/yanivdll/prodissues) that
    includes the content and the HTML template. It means that moving to
    another hosting or SSG is easy.
-   ****Cost**** - running a static site is almost free. All I have to
    pay for is the domain name (\~13\$/year) and the Amazon S3
    storage (\~0.5\$/month).

## Things that I don't like 

-   ****Generating the HTML pages is slow**** - every time I'm adding a
    new post, or editing an existing one, I have to regenerate the site.
    This process takes time, and gets longer as I accumulate more and
    more posts. Pankaj More put it nicely in his article [Static Site
    Generators Focus On The Wrong
    Thing](http://blog.pankajmore.in/static-site-generators-focus-on-the-wrong-thing).
-   ****Too much friction**** - no matter how automated my process is,
    it's still cumbersome. Just take a look at all the touch-points in
    my publishing workflow:


![posting-workflow-with-pelican.png](http://media.prodissues.com/images/2016/01/posting-workflow-with-pelican.png)


-   ****No mobile support**** - since Pelican runs on the desktop, I
    have no way to write a post on my iPhone and publish it directly to
    my blog. This adds friction to my writing workflow, and hinders me
    from writing more spontaneously.
-   ****Maintenance and site administration**** - I'm getting tired of
    running 2 terminals at all times, just to regenerate the site and
    keep a development server live.
-   ****Slow iterations**** - adding new functionality, improving
    existing one, or making some UI changes takes a lot of time. Again,
    this is valuable time that I prefer spending on writing.
-   ****Flaky org-mode integration**** - I write most of my posts in
    [Org-mode](http://orgmode.org/), using Emacs. Pelican and org-mode
    doesn't work very well together. While there's a plugin for Pelican
    that reads org files(org\_reader), it relies on my
    Emacs configuration. And since I'm experimenting with Emacs a lot,
    this plugin constantly breaks. And when that's happens, most of my
    posts (those that are in org-mode), won't be generated, and
    disappeared from the site.


![error-make-html.png](http://media.prodissues.com/images/2016/01/error-make-html.png)

<span class="figure-number">Figure 2:</span> Working with org and
Pelican isn't a smooth sail


And when it comes to Wordpress, here are the goods and the bad:

## The Goods

-   ****The writing experience**** - starting, writing and publishing a
    new post is frictionless.
-   ****Functionality**** - comments, search, categories and tags
    filtering, social functionality, and advanced post status
    management, are all part of the platform.
-   ****Native commenting system**** - if you'll read [this
    post](http://prodissues.com/2015/11/adding-a-commenting-system.html),
    you'll find that I'm not a big fan of disqus. Using the native
    Wordpress commenting system is a big plus for me.
-   ****One dashboard**** - I use Google analytics to monitor traffic,
    and disqus dashboard to manage comments. I like the idea of getting
    all this information in one place. Additionally, I currently don't
    have a way to manage posts and drafts, since they are just files in
    a folder. Having a dashboard where I can take a glimpse and see how
    my site looks like is another benefit.
-   ****Community**** - I'm getting warmer to the idea of being part of
    the Wordpress community; of following, and being followed by, other
    interesting bloggers, and having my posts discoverable across the
    Wordpress ecosystem.


## Concerns

-   ****Lack of control**** - that's my biggest concern. When I [left
    Evernote](http://prodissues.com/2015/06/why-i-decided-to-move-away-from-evernote.html),
    I've decided that I'll never use proprietary formats; that I will
    keep my information in plain text. I didn't want my data to be
    reliant on a company that can go bust, or mess up with my it. I'm
    not sure this is the case with Wordpress, because people seem to not
    have issues exporting their blogs and moving elsewhere, and because
    it's open source. So there will always be a way to gain control over
    my data if needed. But still, having a black box that I know not how
    it operates is bothering.
-   ****Complexity**** - I won't be able to wrap my site with a bunch of
    markdown files.
-   ****Cost**** - Wordpress will cost much more, regardless if I use
    Wordpress.com for hosting, or going the wp-admin route.
-   Performance - not high on my priority, at least for now, but still,
    this is one of the main issues people mention when talking about
    their decision to switch from Wordpress to static sites.


## Conclusion

As I'm writing this post, my gut feeling tells me that I've already made
a decision, and that I use this post as a way to rationalize the
decision to myself. ****I'm going to migrate my blog to Wordpress****.

I'll do it gradually, though, and make a "cut-off" only when I'm sure
the benefits out-weight the drawbacks. I've already opened a blog in
Wordpress. It uses the default settings and URL
([yanivgilad.wordpress.com](http://yanivgilad.wordpress.com/)). I will
start pushing there everything I post[^3] some
stuff there, including new posts that I push to pelican, to play around
with the system, and see how it feels.

## Updates

1.  Fixed the issue.
2.  Pelican refuses to generate this post. There's probably something
    wrong with the org-reader plugin, or my Emacs config... but that's
    an example for the friction and site administration work I'm trying
    to avoid.

[^1]: For a list of almost every SSG available, check out
[StaticGen](https://www.staticgen.com/).

[^2]: Martin, by the way, decided to move to Wordpress.

[^3]: I installed [org2blog](https://github.com/punchagan/org2blog/) in my
Emacs, and plan to use it to push my org-mode based posts to Wordpress.