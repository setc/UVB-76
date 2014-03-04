#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Sebastian'
SITENAME = u'UVB-76'
SITESUBTITLE = u'Radiando futuro'
SITEURL = 'http://UVB-76.github.com'

TIMEZONE = 'Europe/London'
DEFAULT_DATE_FORMAT = '%a %d %b %Y at %I:%M%p'
DEFAULT_LANG = u'es'

#Aesthetics and blog design
DEFAULT_PAGINATION = 5
NUM_FULL_ARTICLS = 1

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/infrafrequency'),
          ('Github', 'https://github.com/SebastianTorrente'),
          ('Tumblr', 'https://infrafrequency.tumblr.com/'))

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#Images and robots needs no parse
STATIC_PATHS = [
    'pictures',
    'extra/robots.txt']
