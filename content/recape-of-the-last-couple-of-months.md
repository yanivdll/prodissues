Title: What I've Been Working On Lately - Recap
Date: 2017-01-11 23:40
Author: yaniv
Category: design, product, Uncategorized
Tags: design, illustrator, inkscape, python, sketch, workflows
Slug: recape-of-the-last-couple-of-months
Status: published

I didn't write for a while[^1]. And it's not that nothing had happened. The opposite... so much learning and new experiences that I didn't find the time to log. No, it's not a lack of time, but rather not internalizing how important it is to stop, asses and capture what I'm learning as I go.

But it's better done late than never[^2]. So here's a list of projects I've been working on, in no particular order, followed by the list of new skills I've learned.

## Projects

### Outbrain News Brief for Alexa

This is a simple skill for Alexa, that reads summaries of top news stories. So as a user, you have to add this skill to Alexa, and can then ask Alexa "what's in the news". Alexa then calls a web service, which I developed. This web-service calls Outbrain and ask for the latest news (using the [Sphere platform](https://developers.sphere.com)). It then sends the articles it gets from Outbrain to a summation service ([Agolo](https://www.agolo.com/)), and returns them back to Alexa, which then reads the summaries to the user.


### Outbrain skill for Alexa

Similar to the skill above[^3], but with more functionality. This is actually the initial stage of a conversational experience, where users will be able to interact with Alexa to get personalized news stories. So users will be able to guide Alexa through conversation to article from site, or on topic they are interested in, or discover new content based on their interest graph. Here's a simple sequence diagram that illustrating the current user flow:


![sequence-diagram.jpg](http://media.prodissues.com/images/2017/01/sequence-diagram.jpg)


### My Clipboard 

![alexa-clipboard-icon.png](http://media.prodissues.com/images/2017/01/alexa-clipboard-icon.png)


Now that's where things become more interesting, working on my stuff... This is a skill for Alexa that serves as your clipboard. You can say" Alexa, ask my clipboard to remember 212 322 4432" and she'll remember this phone number for you. "Alexa ask my clipboard what's in my clipboard" (yeah, redundant, I know...) and she'll repeat the phone number for you.

Why is it helpful? imaging that you're on the phone and can't take a note, or fine a pen to write one down... let Alexa handling it for you... But if you think about a smarter clipboard, one that takes keys and values, you can do much more interesting stuff. For example, ask Alexa to remember that you put your passport in the top drawer. Later on, you can ask her where did I put the passport. But that's a longer term functionality... I first need to finish the current iteration and get it public (it's not at the time of writing this...).



### [Baby Weatr](http://m.me/1800370993514871)

![Artboard\_1v2.png](http://media.prodissues.com/images/2017/01/Artboard_1v2.png){width="150px"}

Baby Weatr is a Facebook Messenger app[^4] that helps parents decide how to dress their kids appropriately for the weather. Well, it designed around my lack of any skill to translate weather into baby wear. So to make sure I'm not endangering our daughter, I decided to build this decision support app.

I'm working on it together with a friend, but this was an opportunity to tie together a lot of the things that I like, and always wanted to use more, such as coding and design[^5]. Initially we tried to outsource the design work, but working with chip freelancers produced deliverable at the quality we paid for, meaning bad. On the other hand, hiring capable designer is expensive. So, I decided to hone on the opportunity to connect with the right side of my brain, and design the first version of the app myself.

Baby Wear is live on Messenger now, so if you need help dressing up your baby - I would love to get your feedback...

[Try Baby Weatr](https://m.me/1800370993514871?ref=Welcome)


### [Dlog](https://yanivgilad.wordpress.com)

While working on the projects above, I did quite a bit of coding. What's
more, this time I coded almost professionally (some of  what I built is
going to be used by my company...).

I found that I need to log what I'm doing, so I can backtrack if needed, and won't make the same mistakes twice. I found that it also accelerated my learning (similar to how writing does...). Git commit, or inline commenting weren't enough, as I wanted to capture not only the outcome of my thinking, research, trail and error and refactoring. But rather, I wanted to put capture my deliberations and place bread crumbs as I go. I wanted to be able to read back and understand why I made certain decisions. For example, why I selected one data structure and not another, how do I start a flask project, and how do I run a flask app and make it reload every time I make a change.

And so I started to maintain a file called development log, or dlog. I keep it open as part of my workspace and include it in my git repository. Here's an example of how it looks like (the dlog is in the bottom right quadrant):


![](http://media.prodissues.com/images/2016/11/Screen_Shot_2016-11-29_at_12.50.16.png)

I thought that might be something that other developers find helpful, and put it on a separate blog ([here](https://yanivgilad.wordpress.com)). I'm contemplating with the idea of opening this blog for others, with the assumption that if many developers log their process, it will serve as a new form of knowledge repository, stack-overflow extension, or companion to readme documentation.


## Things I've learned

### ~~Chatbots~~ Messenger Apps

Well that's not new for me... my team is dedicated to messaging apps for awhile now. I think I mentioned before that we're responsible for the CNN app on Messenger and Kik, as well as for the apps of other notable publishers. What I *did* learn is how to view these type of apps as the best way to develop an MVP, and how you can build a full experience with building blocks, and minimum amount of code, or back-end services.

I'm used Chatfuel[^6] as the content management system for the Baby Weatr app, and love the way I can control the behavior of the app, and build it to match the way I'm thinking about flows. Here's how the Baby Weatr app looks like within Chatfuel: ![chatfuel-baby-weatr.png](http://media.prodissues.com/images/2017/01/chatfuel-baby-weatr.png)


### Assistant devices

Assisted device are the conversational version of messenger apps. Here, a user can interact with a device with voice, rather than with text. I've been working with Alexa on the skills I mentioned above. I also experimented with Google Home, and their api.ai platform.

I think that these experiences are the real revolution in AI and conversational design, and messaging apps, or chatbots are just a stop in the way. I suspect that FB is going to kill their (less than) year old platform, and bet on live video, VR and maybe voice recognition. Right now the messenger apps are like a ghost town, Much more to say about that, and about what messenger apps *are* good for (hint: MVP). I'll keep that to another post.

### Python

Python isn't new to me. I use it occasionally to write scripts to streamline my workflows, or automate tedious manual work. ([Automate the Boring Stuff with Python](https://automatetheboringstuff.com) was the book that got me started with python. Highly recommended.)

But this is the first time I've used python for real products and services. Using it more intensely I've learned how friendly the language is, and how well it fits the way I think about code. I wrote so much, that even google took note, and invited my to the google coding challenge[^7], mistaking me with a real developer :-).

![google-code-challange.jpg](http://media.prodissues.com/images/2017/01/google-code-challange.jpg)


#### Flask

That's the backbone of almost every one of the projects I listed above. [Flask](http://flask.pocoo.org), and it's Alexa extension - [Flask-Ask](https://alexatutorial.com/flask-ask/), are super easy and intuitive packages that help creating web services. I created a template (TODO: push this template to GitHub) and I use it as a starting point with new projects.


### Design

Now, that were my passion is at these days. I've just finished a 12h [Illustrator course](https://www.udemy.com/adobe-illustrator-cc-tutorial/learn v4/) in Udemy, and in the middle of a... [Illustrator 4 Fashion](https://www.udemy.com/learn-to-draw-fashion-with-adobe-illustrator-cc-beginners/learn/v4/) class. All I think about are shapes and colors, and how I can make them in Adobe Illustrator, my hands are glued to the new [Intous Pro](https://us-store.wacom.com/Product/intuos-pro-s01#/undefined1) I've just bought.

In a way, I'm where I wanted to be when I did my bachelor degree - code and design (I graduated as a software engineer, with focus on machine learning and... graphic design).

But in my journey to Illustrator I actually made two stopped, in Inkscape and Sketch. I started with Inkscape, which is great. It's easy to learn and very powerful. What I like most with Inkscape is the control over the creation and modification of paths, which is way easier and more intuitive than Sketch and Illustrator. I did most of the clothing items to Baby Weatr using it, and posted samples of these designs in a [previous post](http://prodissues.com/2016/12/some-illustration-fun.html).

But Inkscape lacks in layout and layer management. I also missed smart guides, which makes the interface design much controllable. And so I've started to learn [Sketch](https://www.sketchapp.com).

I love Sketch's workflow, as well as the way it lets me organize design assets alongside my artboards. But, it's not a replacement to Inkscape when it comes to actual illustrations. What I ended up doing is creating the cloth items' illustrations in Inkscape, and importing them into Sketch, where I did the layout created the sets of outfits.

Here's how the Baby Weatr project looks like in Sketch: 

![sketch-outfits-page.png](http://media.prodissues.com/images/2017/01/sketch-outfits-page.png)

![sketch-cloth-items.png](http://media.prodissues.com/images/2017/01/sketch-cloth-items.png)

And then, as I drawn deeper and deeper into design, I've started to learn more about Adobe Illustrator. I tried it while using Inkscape and Sketch, but it seemed too complex, and inaccessible to me. But the more complex it seemed, the more attracted to it I became (no wonder I use Emacs...). When I finished all the clothing sets I needed for the beta launch of Baby Weatr, I decided to get serious and learn Illustrator. After all, it is *the* tool for designers...

And as I mentioned, 150 episodes later that took 15 hours and span over 3 course, I'm at a point where I feel comfortable with the tool, and starting to do art and design work in it.

Phooo, there was a lot of catching up I needed to do... but it feels good to look at that list and appreciate all the things that I had the chance to learn and experiment with.

[^1]: And now, just to make sure this post is going to get published, I used [one of my hacks](http://prodissues.com/2016/10 another-change-to-my-writing-workflow.html), and put it on scheduled publishing...

[^2]: And no, there's no new year resolution involved in this writing. I don't
like this practice, and don't set those resolutions...

[^3]: This skill is still in development, so not public and can't be added to
Alexa yet.

[^4]: aka chatbot, but I denounce the term, because it's lame...

[^5]: I graduated as a software engineer, with a focus on machine learning
and... graphic design.

[^6]: They were actually a fierce competitor when we tried to get the CNN
project :)


[^7]: I completed several stages, but didn't go all the way, because I had
other things to work on, and I'm not going to make a career switch...