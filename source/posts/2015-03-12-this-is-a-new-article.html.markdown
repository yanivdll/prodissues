---
title: Another Example for Blog Post
date: 2015-03-12 01:38 UTC
tags: test, post
---

**The problem:**
Every evening I leave work at about 6pm. I want to buy bubble tea to Michal. Everytime its the same order. They know me (and her). Yet, it always takes the same time to prepare, about 5 minutes, no matter when I come and who's in the counter. 

<!--more-->

The bubble tea place is right on y way from work home. But many times (acctually most of the time) I cann't stop to buy, because I leave worak just at time so I can get home for Noam's bath time.

I don't call in advance, or using pick up services, because it takes time, and I'm not sure that they even take orders over the phone.

I want to be able to push a button and have a drink ready for pick up 15 minutes later, when I pass the store on my way home.

I want to pay in advance.

I want my usuall.

**The idea:**
A service, where users can login, define their 'usuals', provide payment information, and define pickup timeframe (for example - 20 minutes pickup after _pusing the botton_)

Those users can then trigger their usual with one click.

Once triggered, payment is made, and the _usual_ get ordered, and set to be ready after the configured time.

**A transaction flow**
- User register with the service
- User define a _usual_ and provide payment information
- User is then trigger a *usual* request.
- Service communicating with the business that should fulfill the order.
- Order is being made on behalf of the user:
- Order details is being communicated
- Time for serving
- Payment is being made
- User picks up the order after a set time (according to whet this user defined when creating the trigger).

**Challenges**
- Need to include all the small businesses
- *Possible solution*
- add most popular places at first
- start in a defined geo
- allow businesses to add themselves
- All menus of the places
- *Possible solution*
- Scrap menus (menu pages, seamless)
- Payment
- Processing
- Paying the SMB
- *Possible solution*
- Apple pay
- Bit coins

**The innovation**
- We don't deal with the service itself.
- We're a platform where users can login to define their proifil and usuals.
- We then provide API and oAuth. Other services can then connect to ours to provide support.

**How to start?**
