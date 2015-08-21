#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Yaniv Gilad'
SITENAME = u'prodissues'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Default attributes for a post
DEFAULT_METADATA = {}

# Do not publish articles set in the future
# WITH_FUTURE_DATES = False
# XXX Temporaryly set this option to True while we wait a fix in Pelican 3.6.
# See: https://github.com/getpelican/pelican/pull/1525
WITH_FUTURE_DATES = True

# Create a create per-year, per-month archives
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'
PAGE_PATHS = ['pages']

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
	('Python.org', 'http://python.org/'),
	('Jinja2', 'http://jinja.pocoo.org/'),
	('You can modify those links in your config file', '#'),)

# Menu items
MENUITEMS = (('Posts', '/'),
	('About', '/about/'))

# Social widget
SOCIAL = (('tweeter', 'http://twitter.com/prodissues'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Disable disable caching in Dev
LOAD_CONTENT_CACHE = False

THEME = '/Users/ygilad/dev/pelican-themes/prodissues_simple'