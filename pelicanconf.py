#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import sys

sys.path.append(os.curdir)

from collections import OrderedDict

AUTHOR = u'@lmorillas'
SITENAME = u'Congreso de Fisiología'
SITEURL = 'http://localhost:8000'

META_DESCRIPTION = '''Un proyecto educativo organizado por los alumnos de 2º de medicina 
de la Universidad de Zaragoza con la ayuda de los profesores del departamento de fisiología'''

META_KEYWORDS = ['congreso fisiología', 'congreso', 'medicina', 'alumnos']

TIMEZONE = 'Europe/Madrid'
THEME = 'themes/malt'
MALT_BASE_COLOR = 'blue'

SITE_LOGO = 'images/logo/estudiante.png'
#SITE_LOGO = 'images/logo/cartel2.jpeg'
SITE_LOGO_MOBILE = 'images/logo/estudiante.png'


STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

WELCOME_TITLE = 'VIII Congreso de Fisiología'
WELCOME_TITLE2='@unizar'
WELCOME_TEXT = '2, 3 y 4 de Mayo de 2017'
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

GITHUB_REPO = "http://github.com/lmorillas/congreso_fisiologia"
GITHUB_BRANCH = "gh-pages"
TWITTER = "@lmorillas"
OPEN_GRAPH_IMAGE = "/images/logo/estudiante.png"

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
    {
        "title": "Acerca de",
        "href": "acerca_de",
    },
]


SOCIAL_LINKS = (
    {
        "href": "https://www.instagram.com/viiicongresofisiologia/",
        "icon": "fa-instagram",
        "text": "Instagram",
    },
    {
        "href": "https://www.facebook.com/VIII-Congreso-De-Fisiolog%C3%ADa-Unizar-1811411632515573/",
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
                        "href": "programa",
                    },
                ],
            },
            {
                "title": "¿Dónde?",
                "icon": "fa-map-marker",
                "text": "<strong>Lugar:</strong> Facultad de Medicina, Universidad de Zaragoza <br>" +\
                        "<strong>Fecha:</strong> 2, 3 y 4 de Mayo de 2017",
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

CONGRESOS_ANTERIORES = [
   { "url": "http://www.unizar.es/congresofisiologia/VI%20Congreso%20de%20fisiologia%202/V%20congreso%20fisiologia/IV%20Congreso%20de%20%20Fisiologia%20FMZ/Otros/primercongreso/default.html",
     "logo": "congresoI.jpg",
     "nombre": "I Congreso"
   },
   { "url": "http://www.unizar.es/congresofisiologia/VI%20Congreso%20de%20fisiologia%202/V%20congreso%20fisiologia/IV%20Congreso%20de%20%20Fisiologia%20FMZ/Otros/segundocongreso/index.htm",
     "logo": "congresoII.jpg",
     "nombre": "II Congreso"
   },
   { "url": "http://www.unizar.es/congresofisiologia/VI%20Congreso%20de%20fisiologia%202/V%20congreso%20fisiologia/IV%20Congreso%20de%20%20Fisiologia%20FMZ/Otros/index3.html",
     "logo": "congresoIII.jpg",
     "nombre": "III Congreso"
   },
   { "url": "http://www.unizar.es/congresofisiologia/VI%20Congreso%20de%20fisiologia%202/V%20congreso%20fisiologia/IV%20Congreso%20de%20%20Fisiologia%20FMZ/inicio.html",
     "logo": "congresoIV.jpg",
     "nombre": "IV Congreso"
   },
   { "url": "http://www.unizar.es/congresofisiologia/VI%20Congreso%20de%20fisiologia%202/V%20congreso%20fisiologia/index.html",
     "logo": "congresoV.jpg",
     "nombre": "V Congreso"
   },
   { "url": "",
     "logo": "congresoVI.jpg",
     "nombre": "VI Congreso"
   },
   { "url": "",
     "logo": "congresoVII.jpg",
     "nombre": "VII Congreso"
   },
]

from themes.malt.functions import *
