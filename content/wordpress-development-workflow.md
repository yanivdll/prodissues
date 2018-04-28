Title: My WordPress Development Workflow
Date: 2016-02-10 00:00
Author: yaniv
Category: geeking
Tags: development, Wordpress
Slug: wordpress-development-workflow
Status: published

I currently use a child-theme for this site[^1], its parent being
[twentysixteen](https://wordpress.org/themes/twentysixteen/). I keep
modifying this theme on my local machine and push updates to my live
site. But in parallel, I want to start building a completely new theme,
based on the starting [\_s](http://underscores.me/) theme. I'm
uncomfortable developing this new theme within the same local
environment; I want, instead, to create a playground where I can
experiment, knowing it's completely isolated from my production
environment.

<!--more-->

With that goal in mind, I installed a second instance of WordPress on my
local machine, and now I have 3 environments - production(that's where
my live site reside), staging and development.

## Running two WordPress instances on the same machine

### Folder structure

Initially, I had WordPress installed in a folder called `wordpress`. To
prepare for the second install, I created the following hierarchy:


![wp-folders.png](http://media.prodissues.com.s3.amazonaws.com/images/2016/02/wp-folders.png)

I moved the content of my original WordPress to the
`/prodissues-staging` folder. I then had to go to
[MAMP](https://www.mamp.info/en/) and change the "Document Root"
setting, to point to the new location, so that when I visit
`localhost:8888`, I still land on my site.


![mamp-prodissues-staging.png](http://media.prodissues.com.s3.amazonaws.com/images/2016/02/mamp-prodissues-staging.png)

Next, I downloaded WordPress to the `prodissues-dev` folder. To start
the installation process, I had to go back to MAMP and change the
"Document Root" to point to that folder:


![mamp-prodissues-dev.png](http://media.prodissues.com.s3.amazonaws.com/images/2016/02/mamp-prodissues-dev.png)

At that point I was ready to install WordPress in my development
environment. This is the same process as installing WordPress for the
first time, including the creation of a new database[^2]. To refresh your memory on how to do it, here's WordPress
["Famous 5-Minute Install"](https://codex.wordpress.org/Installing_WordPress#Famous_5-Minute_Install)
guide.

## Switching between environments

I now had two WordPress installations on my local machine (and one
hosted). Switching from one to the other is as simple as changing the
"Document Root" in MAMP, as was shown above.

What left to be done is to define a workflow that will help me keeping
the different environments fresh, while making sure the live site (i.e.
production environment) is safe from what's going on in the development
environment.

## Development workflow 

I now have 3 WordPress environments:

-   Production (hosted)
-   Staging (local)
-   Development (local)

My plan is to make sure that staging is always in sync with production.
I'll build my new theme in the development environment, and push it to
staging when it's ready. If everything works fine in staging (which is,
again, almost identical to the live site) then I'll push the new theme
to production.

Here's a sketch that illustrates the separation and interaction among
the 3 environments:


![wp-environments.jpeg](http://media.prodissues.com.s3.amazonaws.com/images/2016/02/wp-environments.jpeg)

And here's the logic behind this architecture:

-   The most important resource that I would like to protect is the
    production database, since it holds the content of my blog. I might
    be missing something here, but I see no reason to ever override it
    with a version of the database from other environments. Therefore,
    the production database can only be pulled to the staging or
    development environments[^3].
-   I shouldn't push files from development directly to production. I
    should move them instead to staging. This will protect my live site
    from un-tested or broken code.
-   Staging is where new code is tested. From there it can be pushed
    only one way - to production via ftp. Again, there's no upload of
    the database to production.

This one-way streets architecture should give me the peace of mind to
build and breaking stuff, knowing that whatever I do won't affect the
other 2 sane environments.

## Open question:

-   Is there any reason that I haven't thought of to push database from
    staging to production?

[^1]: Feel free fork it on GitHub -
<https://github.com/yanivdll/twentysixteen-child>

[^2]: With one exception - the name of the new database should be unique. I
called mine `prodissues-dev`.

[^3]: I use [wp-sync-db](https://github.com/wp-sync-db/wp-sync-db) to pull the
database and files from production to dev and staging.