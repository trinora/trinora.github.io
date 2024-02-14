AUTHOR = 'Trinora Team'
SITENAME = 'Trinora Software'
SITEURL = ""

PATH = "content"
TIMEZONE = 'America/Edmonton'
DEFAULT_LANG = 'en'
THEME = 'themes/pelican-theme-html5up-hyperspace'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME_HOMEPAGE_INTRO_PAGE = "landing"
THEME_MENU_ONLY_MENUITEMS = True
THEME_HOMEPAGE_INCL_ARTICLES = False

MENUITEMS = (
    ('Website', 'https://trinora.software/'),
    ('Github', 'https://github.com/trinora'),
)

# Blogroll
LINKS = None

# Social widget
SOCIAL = None

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

BIND = '0.0.0.0'