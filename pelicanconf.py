#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Corey Richardson'
SITENAME = u"This Week in Rust"
SITEURL = 'http://this-week-in-rust.org'

SOURCE_URL = 'https://github.com/cmr/this-week-in-rust'

if '1' == os.environ.get('TWIR_NEWSLETTER_THEME'):
    THEME = 'themes/newsletter'
    css_path = os.path.join(os.path.dirname(__file__), 'themes', 'newsletter', 'static', 'css')
    with open(os.path.join(css_path, 'ink.css')) as f:
        CSS_INK = f.read()
    with open(os.path.join(css_path, 'main.css')) as f:
        CSS_MAIN = f.read()
else:
    THEME = 'themes/rusted'

PLUGIN_PATHS = ["plugins"]
PLUGINS = ['assets']

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'atom.xml'
CATEGORY_FEED_ATOM = 'categories/%s/atom.xml'

DEFAULT_PAGINATION = 10

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

ARCHIVES_SAVE_AS = 'blog/archives/index.html'

CATEGORY_URL = 'categories/{slug}/'
CATEGORY_SAVE_AS = 'categories/{slug}/index.html'

LANDING_PAGE_ABOUT = {
        "title": "Cataloging the Rust community's awesomeness",
        "details": """
A weekly newsletter about Rust and the Rust community, with bonus content
scattered about.
"""
}

MD_EXTENSIONS = ['headerid']
