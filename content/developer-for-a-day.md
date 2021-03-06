Title: Developer for a day
Date: 2015-11-19 05:00
Author: yaniv
Category: code
Tags: emacs, product
Slug: developer-for-a-day
Status: published

Earlier today I demoed a simple search page that I developed as part of
a 24 hour hackathon here at Outbrain. What makes this search page unique
is that it uses the Sphere platform [^1] to find
content that isn't only relevant to the search query, but also caters to
the user's interests. So, for example, if I search for "python", I'll
get articles about python, the programming language. If my mom, on the
other hand, do the same search, she'll get articles [like this
one](http://www.cnn.com/videos/us/2015/11/10/alligator-python-photo-florida-dnt-wftx.wftx).

But *what* I developed isn't the subject of this article (I might write
about it in a separate post). What I *do* want to share is my experience
at putting a developer hat for a day. As a product manager, who works
very closely with engineers, this turned out to be an invaluable lesson.

I had no intention of building anything in that hackathon. My plan was
to help and support the hacking teams[^2]. A
few minutes after the hackathon began, though, I thought it will be cool
to build this search page. Unfortunately, at that point there were no
developers around to whom I could pitch my idea. All of them were
already assigned to other teams. But I got this impulse to build
something, so I decided to challenge my lack of development skills, and
form a team of one.

Well, saying that I'm not a developer isn't entirely true. After-all, I
graduated as a software engineer, I understand technology, I can speak
intelligently about software architecture and design patterns, and I was
intimately involved in designing and building the Sphere platform. I
even do some coding in my spare time[^3]. But,
I've never coded with a mission or under a strict deadline. So I
thought, this would be an opportunity to get serious about coding.
Indeed, serious I became, spending the next 24 hours (minus 6 hours of
sleep) hacking my way toward something I'll be proud to present.

Here's how my next 24 hours have looked like:

**10:20am** - 20 minutes into the hackathon I'm having this idea, and
yada yada yada I decide to code.

**10:40am** - I can see what the architecture of the solution should
look like, and what APIs I'll have to use. It's going to be easier than
I thought...

**11:30am** - Hitting a dead-end. My initial approach won't work,
because I don't have access, from the environment I'm using, to the API
I rely on. Need to think of a new direction.

**12:00pm** - Found a new direction. I'm not sure it's the right one,
and I'll have to learn a framework that I didn't use before (well, I
didn't use *any* framework before...), but I'm running out of options,
so I'm taking the chance. I find a tutorial, and hope to learn
everything I need to know before the hackathon is over.

**1:30pm** - Urr... this is the longest tutorial ever, and it's not even
related to the use-case I'm trying to solve.

**2:15pm** - OK, good news and bad news. The good - I finally finished
the tutorial. The bad - I still don't have a clue how to work with this
framework to build what I have in mind.

**3:00pm** - 5 hours have passed, and I still have nothing. What's worse
- people around me have high expectations of me. I have no idea why, but
I know I'm going to disappoint them. I'm loosing my patience, and even
the quietest chatter in the room distracts me. I'm agitated, and my fuse
shortens by the minute. I hope no one will talk to me. I need silence.
Maybe I should put headphones on, or go to a secluded room...

**4:10pm** - Half a day went by, and I'm farther away from my initial
idea than I was 6 hours ago. Maybe some coffee and fresh air will help
me regain energy and spirit.

**4:20** - I don't know if it's the coffee or the time off the computer,
but I'm thinking more clearly now. In fact, I have an idea. I need to
run back to the office.

**5:30pm** - I have a working solution! It looks awful, but works....
all I have to do now is take care of the front-end. Easy breezy.

**9:15pm** - **I hate CSS**. I'm about to loose my mind. I must eat.

**10:00pm** - I need to have *some* sleep. I'm sure things will look
easier tomorrow.

**8:10am** - CSS is still CSS.

**9:55am** - 5 minutes to my demo. With some help, hand-holding and a
lot of duct-tape my work is somewhat presentable. I hope people see the
potential, and won't get caught-up with the UI.

**10:10am** - I've just presented my thing. **I feel awesome**. I built
something and got people's applause.

Now, what did I learn from this schizophrenic experience:


## I don't want to be a developer.

Yeah, as simple as that. I'll keep doing it as a hobby, but I'll never
do it professionally. I mean, I love the problem solving, and creating
something with my own hands is amazing. But, getting sucked into the
smallest of details, spending hours trying to figure out what I did
wrong, only to find a missing `;`, and wasting tons of time on
configuration before I can do *anything*, make me go nuts...

OK, so as this door is now closed, what did I learn about coding that
will help me understand engineers better?



## Coding requires focus

Soooo much of it. Even the slightest distraction can throw your thought
process miles away. It then takes a lot of time to regain your thoughts,
and get back to where you were before. I now understand even better
Joel's ["Human Task Switches Considered
Harmful"](http://www.joelonsoftware.com/articles/fog0000000022.html)
post.


## Tools are important

Don't ask why, but I've started to learn
[Emacs](https://www.gnu.org/software/emacs/) recently, and so far I love
it. But, Emacs isn't the most dummy proof app out there. Here's a funny
chart, that actually stops being that funny when you start learning
Emacs:


![3251176498\_c3485a55fb.jpg](http://media.prodissues.com/images/2015/11/3251176498_c3485a55fb.jpg)

So, since I'm somewhere at the bottom of the learning curve still, I
thought this hackathon would be an opportunity to learn the tool better
and faster. But as soon as time started to press on me, and at the first
instance when I didn't know how to do something in Emacs that was
trivial in other tools, I closed it and opened the other tools I feel
comfortable with ([Sublime](https://www.sublimetext.com/) and
[CodeRunner](https://coderunnerapp.com/)).


## Knowing what's the expected outcome is key 

Having a clear idea of what my end product should do, and to some extent
- how it should look like, was crucial. I had so much to learn in a very
short time, but knowing what my end goal was kept me focused. It also
helped me stay on course and learn only what was relevant to getting my
project done (otherwise I have the tendency to drift away quickly).

And lastly, I experienced first hand how deadlines and quality \[don't\]
play \[well\] together:


## Code becomes crappier as deadline approaches

You might think that my experience isn't a good enough example, and I
might agree. I'm just saying that now I can better relate to this
[\#NoDeadlines](https://twitter.com/hashtag/NOdeadlines?src=hash) trend.

If you're involved, at any capacity, in product development, you already
know this lesson, because crappy code keeps bouncing back at you and
eats the time and resources you need in order to build new stuff. Don't
be fooled by fancy terms, such as "tech-debt" and "refactoring" - these
are politically correct ways to refer to crappy code. And the stricter
the deadlines, the more of it you'll get[^4].

So with that, I'll put my developer hat down. It's too big for me...

[^1]: Check out the platform [here](http://developers.sphere.com/#/), and
leave a comment if you're interested to learn more.

[^2]: There were 19 internal and external teams hacking.

[^3]: In case you're interested, here's [my GitHub
account](https://github.com/yanivdll).

[^4]: No, it doesn't mean I won't ask for time-lines and set deadlines in the
future...