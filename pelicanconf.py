#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import sys

sys.path.append(os.curdir)

from collections import OrderedDict

AUTHOR = u'@lmorillas'
SITENAME = u'Congreso de Fisiología'
SITEURL = '/'

META_DESCRIPTION = '''Un proyecto educativo organizado por los alumnos de 2º de medicina 
de la Universidad de Zaragoza con la ayuda de los profesores del departamento de fisiología'''

META_KEYWORDS = ['grupy-df', 'python', 'brasilia', 'desenvolvimento']

TIMEZONE = 'Europe/Madrid'
THEME = 'themes/malt'
MALT_BASE_COLOR = 'blue'

SITE_LOGO = 'images/logo/estudiante.png'
SITE_LOGO_MOBILE = 'images/logo/estudiante.png'

#STATIC_PATHS = ['images', 'extra/CNAME']
#EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

WELCOME_TITLE = 'Bienvenido al VIII Congreso de Fisiología'
WELCOME_TEXT = ''
SITE_BACKGROUND_IMAGE = 'images/banners/pilar.jpg'
FOOTER_ABOUT = '''El grupo de alumnos de 2º ...'''

DEFAULT_LANG = u'es'

ARTICLE_URL = 'blog/{slug}'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'

CATEGORIES_URL = 'blog/categorias'
CATEGORIES_SAVE_AS = 'blog/categorias/index.html'
CATEGORY_URL = 'blog/categorias/{slug}'
CATEGORY_SAVE_AS = 'blog/categorias/{slug}/index.html'

TAG_URL = 'blog/tags/{slug}'
TAG_SAVE_AS = 'blog/tags/{slug}/index.html'
TAGS_URL = 'blog/tags'
TAGS_SAVE_AS = 'blog/tags/index.html'

AUTHOR_URL = 'blog/autores/{slug}'
AUTHOR_SAVE_AS = 'blog/autores/{slug}/index.html'
AUTHORS_URL = 'blog/autores'
AUTHORS_SAVE_AS = 'blog/autores/index.html'

INDEX_SAVE_AS = "blog/index.html"

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None

DEFAULT_PAGINATION = False

PLUGIN_PATHS = ['./.plugins']
PLUGINS = [
    'better_figures_and_images',
    'sitemap',
]

RESPONSIVE_IMAGES = True
PYGMENTS_STYLE = "perldoc"
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.8,
        'indexes': 0.2,
        'pages': 0.7
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'monthly'
    },
}

GITHUB_REPO = "http://github.com/grupydf/grupydf.github.io"
GITHUB_BRANCH = "pelican"
TWITTER = "@grupydf"
OPEN_GRAPH_IMAGE = "/images/logo/logo-inv.png"

# Navbar Links
NAVBAR_HOME_LINKS = [
    {
        "title": "Programa",
        "href": "programa",
    },
    {
        "title": "Inscripción",
        "href": "inscripcion",
    },
    {
        "title": "Organizadores",
        "href": "organizadores",
    },
    {
        "title": "Colaboradores",
        "href": "colaboradores",
    },
    {
        "title": "Congresos anteriores",
        "href": "anteriores",
    },
]

NAVBAR_BLOG_LINKS = NAVBAR_HOME_LINKS + [
    {
        "title": "Categorias",
        "href": "blog/categorias",
    },
    {
        "title": "Autores",
        "href": "blog/autores",
    },
    {
        "title": "Tags",
        "href": "blog/tags",
    },
]

SOCIAL_LINKS = (
    {
        "href": "https://telegram.me/joinchat/AG9QCABLx9wgYM1bcoGxgQ",
        "icon": "fa-paper-plane",
        "text": "Telegram",
    },
    
    {
        "href": "https://twitter.com/",
        "icon": "fa-twitter",
        "text": "Twitter",
    },
    {
        "href": "https://www.facebook.com/groups/",
        "icon": "fa-facebook",
        "text": "Facebook",
    },
)

MEMBROS = OrderedDict()

MALT_HOME = [
    {
        "color": "blue-grey lighten-5",
        "title": "Nuestro congreso",
        "items": [
            {
                "title": "¿Qué es?",
                "icon": "fa-users",
                "text": "Un proyecto educativo organizado por los alumnos de " +\
                    "2º de medicina de la <em>Universidad de Zaragoza</em> con la ayuda " +\
                    "de los profesores del departamento de fisiología. " +\
                    "¡<strong>Os esperamos</strong>!",
                "buttons": [
                    {
                        "text": "Más ...",
                        "href": "comunidad",
                    },
                ],
            },
            {
                "title": "¿Dónde?",
                "icon": "fa-map-marker",
                "text": "Lugar: <br> " +\
                        "Fecha: ",
                "buttons": [
                    {
                        "text": "Inscríbete",
                        "href": "inscripcion",
                    },
                ],
            },
            {
                "title": "Actividades",
                "icon": "fa-th-list",
                "text": "Estas son las actividades previstas para esta edición "  +\
                        "...",
                "buttons": [
                    {
                        "text": "Programa",
                        "href": "programa",
                    },
                ],
            },
        ]
    },
]

from themes.malt.functions import *
