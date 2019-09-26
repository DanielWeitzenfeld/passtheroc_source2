#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Dan Weitzenfeld'
SITENAME = 'passtheroc'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%b %d, %Y'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

THEME = '/Users/Weitzenfeld/PycharmProjects/pelican-themes/pelican-octopress-theme'
PLUGIN_PATHS = ['/Users/Weitzenfeld/PycharmProjects/pelican-plugins']
PLUGINS = ['assets', 'sitemap', 'gravatar', 'pelican-ipynb.markup']

MARKUP = ('md', 'ipynb')

DEFAULT_PAGINATION = False

TWITTER_USER = 'weitzenfeld'
TWITTER_FOLLOW_BUTTON = True
TWITTER_TWEET_BUTTON = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Set the article URL.
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'