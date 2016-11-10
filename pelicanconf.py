#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Microcavity Pħotonics Group of Peking University'
SITENAME = 'Microcavity Pħotonics Group'
SITEURL = ''

BOOTSTRAP_THEME = 'cosmo'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

THEME = 'pelican-bootstrap3'

STATIC_PATHS = ['images', 'teaching', 'style.css', 'favicon.ico']

CUSTOM_CSS = 'style.css'

ABOUT_ME = 'Led by Prof. Yun-Feng Xiao, research here centers on both microcavity theories and experiments.'
BANNER = 'images/Raman-laser-sensor.jpg'
BANNER_ALL_PAGES = True
BANNER_SUBTITLE = '@ School of Physics, Peking University.'
HIDE_ARCHIVES_FROM_MENU = True

DISPLAY_TOC_ON_SIDEBAR = True

MATH_JAX = {'source': "'//cdn.bootcss.com/mathjax/2.6.1/MathJax.js'"}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Peking University', 'http://www.pku.edu.cn/'),
         ('School of Physics', 'http://www.phy.pku.edu.cn/'),
         ('American Physical Society', 'http://www.aps.org/'),
         ('Nature Publishing Group', 'http://www.nature.com/'))
SOCIALS = ()

LANG_DISPLAY = {
    'en': 'English',
    'zh': '中文'
}

PLUGIN_PATHS = ['/Users/laser/pelicanplugins/pelican-plugins/']
PLUGINS = ['render_math', 'pelican-toc']

TOC = {
    'TOC_HEADERS' : '^h[2-3]',
    'TOC_RUN'     : 'true'
}



DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
