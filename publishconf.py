#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = '/congreso_fisiologia'   # link en gh-pages
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds.atom'
FEED_ALL_RSS = 'feeds.rss'

DELETE_OUTPUT_DIRECTORY = True


# Following items are often useful when publishing

#GOOGLE_ANALYTICS = ""

