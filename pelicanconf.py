#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Yaniv Gilad'
SITENAME = 'prodissues'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Default attributes for a post
DEFAULT_METADATA = {}

# Create a create per-year, per-month archives
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
	('Python.org', 'http://python.org/'),
	('Jinja2', 'http://jinja.pocoo.org/'),
	('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('tweeter', 'http://twitter.com/prodissues'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = '/Users/ygilad/dev/pelican-themes/aboutwilson'