Title: Self User Testing
Date: 2016-09-27 23:30
Author: yaniv
Category: product
Tags: chatbot, user-experience
Slug: self-user-testing
Status: draft

OK, I'm retracting from my agreement. I just had an experience that proved I wasn't to begin with.

Well, some context will be helpful... let me step back and explain.
Yesterday we had a heated discussion in the team about the usefulness of
showing a description of a post inside a recommendation tile in our
chatbot. Take a look at the screenshot bellow. This is how we
currently display recommendations in [our Facebook Messenger
bot](http://m.me/outbrain):

![fb-chatbot-ctas.PNG](http://media.prodissues.com/images/2016/09/fb-chatbot-ctas.PNG)

Each recommendation comes with a set of metadata: thumbnail, title,
source, and description. The bot.outbrain.com is an ugly appendage
forced by Facebook. Then there are the actions you can take on a
recommendation. Clicking on the thumbnail will open the article in a
webview. Summary will return an auto generated summary[^1], stash will save it for later, and \#{topic} will return more
recommendations from the same topic.

You'll notice that the description in this example (taken from the
article page) isn't great. It's trimmed, and do little to explain what
this story is about. Essentially, it doesn't help me taking a decision
to read or pass on this recommendation.

One of the ideas we came up with was to replace the description with the
reason a user sees a specific recommendation. We call this feature
"Amplify the WHY". In the image above, I probably saw this story because I had read a lot about science and astronomy. The "WHY" in this case should read something like "because you're interested in astronomy".

Showing both description **and** the "WHY" might have been ideal, but
we have limited real-estate to work with, and need to choose one of them.

My team was adamant that we should drop the description and go with the
"WHY". At first, disagreed. "I want to see data first", I said. "Let's run an AB test". "Well, we don't have users yet, so AB testing isn't relevant at that point. Also, it is clear that 'amplifying the WHY' is so much better than a crappy description" was the reply I got. How can one argue with such a compelling reasoning...

Now, circling back to my opening, I'm taking my agreement back.

I woke up at 7am today and wanted to read about the results of the debate yesterday night. I didn't know where I can find this information quickly and succinctly[^2]. I thought about the CNN chatbot, but CNN's top stories are posted only at about 9am. Then I figure, let's try to see if I can find something relevant in our bot.

I typed "hi", and (to my surprise) the first story I got was right on
point -

![fb-chatbot-election-debate.PNG](http://media.prodissues.com/images/2016/09/fb-chatbot-election-debate.PNG)

Then I browsed a little more, and while doing it realized that I skim the descriptions for more context, regardless of the quality of them. I didn't sought completeness or quality, just few more words that will give better idea what the article is about.

"WHY" I get a recommendation, and why it's important to me wasn't
relevant in the context I were in - checking the news.

Summaries weren't relevant in this context, because much like clicking to read the story, it meant "choosing" and focusing on one article, whereas I was still at the decision making stage.

So, what I've learned from observing myself (and in that rare instance,
I acted as a user, rather than a stakeholder) is that description does
have value. 

Definitely not representative experience, but one that makes me rethink
what should be the baseline. And whatever the baseline is, we should put
it to test.

[^1]: Works pretty neatly. Here's the summary for this article in the
picture: "On Tuesday, thousands of people stampeded into a lecture hall
in Guadalajara, Mexico, to hear SpaceX CEO Elon Musk talk about how he
wants to colonize Mars. Another question is how — and if — Musk plans to
prevent Earth microbes from contaminating Mars, and Mars microbes (if
there are any) from contaminating Earth."

[^2]: I don't go to sites to look for news anymore, and rarely Google for news.
And since the extinction of [Zite](https://en.wikipedia.org/wiki/Flipboard), I now realize, I have no idea where I get my news from...