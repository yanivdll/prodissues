#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = u'Yaniv'
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

# Create a per-year, per-month archives
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'
PAGE_PATHS = ['pages']

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
	('Python.org', 'http://python.org/'),
	('Jinja2', 'http://jinja.pocoo.org/'),
	('You can modify those links in your config file', '#'),)

# Menu items
MENUITEMS = (('about', '/about/'),
	('contact', '/about/#contact'),
	('twitter','https://twitter.com/prodissues'),
	('feed','/feeds/all.atom.xml'),
	('drafts', '/drafts/'))

# Social widget
SOCIAL = (('tweeter', 'http://twitter.com/prodissues'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Disable disable caching in Dev
LOAD_CONTENT_CACHE = False

# JINJA_EXTENSIONS = ['webassets.ext.jinja2.AssetsExtension',]

# THEME = '../pelican-themes/aboutwilson'
THEME = 'themes/simple'
ASSET_URL = '/static/'

PLUGIN_PATHS = ['../../pelican-plugins']
PLUGINS = ['assets']

# Org Reader plugin
# ORG_READER_EMACS_LOCATION = "/Applications/Emacs.app/Contents/MacOS/Emacs"
# ORG_READER_EMACS_SETTINGS = "~/.emacs.d/lisp/pelicon-export.el"


# TESTINGS::
# ## disqus
DISQUS_SITENAME = 'prodissues'

# ## Google Analytics
#GOOGLE_ANALYTICS = "UA-60771520-1"