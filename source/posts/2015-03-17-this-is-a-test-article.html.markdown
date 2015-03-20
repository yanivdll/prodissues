---
title: Another Exmample for Blog Post
date: 2015-03-17 17:26 UTC
tags: test, post
---

I've just saw this in Quora[^1]:

> "... a product requirements document shouldn't exist in a Lean Startup context."

and can't disagree more with this statement. This view reflects misconception of what a product requirement document (i.e. spec) is, and what purpose it should serve.

<!--more-->
Outbrain was built on the lean startup methodology. New employees are still getting Eric Ries's book as part of their welcome pack, and everything we build, for better or worst start as an MVP, and evolves though the build-measure-learn cycles. But unfortunately, this methodology is prone to misconceptions, such as the one above. And don't get me started with the abuse people are doing to the concept of MVP...

Take for example a recent issue we've had with our API. At times it returned content recommendations with low quality images or no image at all. This was a bug in our system, which was designed to filter this type of recommendations. We fixed the bug, but wanted to add a bulletproof mechanism. Filtering and replacing recommendations in realtime is very costly in performance, so we had to find a way to "fix" articles that we're about to serve and that don't include  thumbnails. 

The solution we came up with was a pool of images that we'll tap into when we intercept problematic recommendations. Developing this feature is rather simple and doesn't requires more than couple days of work. 

So, to move ahead with the solution I had to send a quick email to our product designer, asking her to come up with about 10 generic images that we'll then use in case we have to inject an image.

I was about send the email, but realized I need to provide some context, otherwise she'll reply with follow up questions - what are those images for? what type of images, etc. To save time and effort, I've added some background and described the problem and what we're trying to solve.

Reading my email again[^2] the email still seem unclear. If I were the product designer reading this email, I would have asked "what do we want users to see and what reaction do we try to evoke?", "how should those images relate to the article they attached to?", "why not use stock images service such as Getty images?" and so on.

No reason to send this email, knowing that it's partial. So, I added information about what we're trying to achieve. I explained that when a story doesn't have a native image, we would like to add one ourselves. This image should "trick" the user into thinking that the image _do_ belong to the recommendation. This effect can be achieved by choosing images with color scheme that blend with the the rest of content in the page, and don't hold too much notable features. A good example if pattern images with warm colors <!--add image-->. Those images help the user ‘glide’ through the thumbnail, without paying too much attention to the content of the image. The user will unconsciously check the mental box that saying ‘this recommendation looks complete’ and move on to inspect other elements, such as the title and the source of the article.

I've linked to a good article in NYT, which explains why stock images are useless[^3], and lastly added few minor requirements, such as minimum image resolutions, and aspect ratio. 


<!--the lesson-->
Guess what my email turned out to be - a **spec**. And here's the point I'm driving at - don't think of it as a document in a certain format. It shouldn't be a 120 pages document that will bore its readers to death. Think of it as a product. The users of this product are those who you count on to build or execute your product, feature, idea. 

Spec is the An efficient way to communicate a thought, idea or aspiration in a way that can be translate by the user


Spec is a way to communicate an idea, feature product from an abstract, high level thought into an actionable and digestible format.

[^1]: Answer to the question ["What should a lean startup functional spec / product requirements doc look like?"](http://www.quora.com/What-should-a-lean-startup-functional-spec-product-requirements-doc-look-like)
[^2]: I'm (trying to be) religious about reading my emails again just before I send them. 90% of the times I'll find a spelling mistake or find better way to express something that I was trying to say. I even have the "undo" feature added to my gmail, and set to 30 sec (the longest duration).
[^3]: [Study Shows People Ignore Generic Photos Online, NYT](http://bits.blogs.nytimes.com/2010/11/02/study-shows-people-ignore-generic-photos-online/?_r=1)