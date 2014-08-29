#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Yingcai FENG'
SITENAME = u'Zenmass'
SITEURL = u'http://fengyc.github.io'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh'

THEME = 'pelican-themes/gum'

PLUGIN_PATHS = ["pelican-plugins"]
#PLUGINS = ["summary"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Weibo', 'http://weibo.com/fyingcai/'),
          ('Github', 'https://github.com/fengyc/'),)

GITHUB_URL = 'https://github.com/fengyc/'

MENUITEMS = (("About","/about"),)

DEFAULT_PAGINATION = 10

SUMMARY_MAX_LENGTH = 40

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
