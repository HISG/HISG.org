# -*- coding: utf-8 -*-
# Django settings for hisg.org.


try:
	 from local_settings import WHICH_ENVIRONMENT
except ImportError, exp:
	 WHICH_ENVIRONMENT = 'production'

if WHICH_ENVIRONMENT == 'development':
	# Django settings on the local dev server for globalgrazer project.
	DEBUG = True
	TEMPLATE_DEBUG = DEBUG

	TEMPLATE_DIRS = ('/Users/travis/Dropbox/hisg-dir/hisgWebsite/hisg/templates')

	import os.path
	MEDIA_ROOT = os.path.join(os.path.dirname(__file__), "site_media")
	MEDIA_URL = '/site_media/'

	ADMIN_MEDIA_PREFIX = '/admin_media/'

	DATABASE_ENGINE = 'mysql'
	DATABASE_NAME = 'hisg3'
	DATABASE_USER = 'hisguser'
	DATABASE_PASSWORD = 'ujCY1qIq8Eto'
	DATABASE_HOST = '192.168.1.153'
	DATABASE_PORT = ''

	GMAPKEY = 'ABQIAAAAKkJhGIDc65pxzIU9FTCsAxTpH3CbXHjuCVmaTc5MkkU4wO1RRhSJDl-ZXe3YDJR5e8jYO-NomOGXqg'
	
	PATHTOKEYS = '/Users/travis/Dropbox/hisg-dir/hisgWebsite/hisg/keys/'
	PATHTOSFPJS = 'http://192.168.1.153:8000/site_media/sfp/sfp_widget.js'
	PATHTOSFP = 'http://192.168.1.153:8000/'
	SITESERVER = 'HISG'
	
	XMLRPCIP = 'http://192.168.1.153:8000/RPC2'
	# GEOS_LIBRARY_PATH = "/Library/Frameworks/GEOS.framework/unix/lib/libgeos_c.dylib"
	
elif WHICH_ENVIRONMENT == 'production':
	# Django settings on the server for globalgrazer project.
	DEBUG = False
	TEMPLATE_DEBUG = DEBUG

	TEMPLATE_DIRS = ('/home/django/domains/hisg.org/hisg/templates')

	MEDIA_ROOT = '/home/django/domains/hisg.org/media/site_media'
	MEDIA_URL = '/site_media/'

	ADMIN_MEDIA_PREFIX = '/admin_media/'

	DATABASE_ENGINE = 'mysql'
	DATABASE_NAME = 'hisg_org'
	DATABASE_USER = 'hisgRDBroot'
	DATABASE_PASSWORD = '14yfsp56'
	DATABASE_HOST = 'hisgrdb.cic0nyfjgak8.us-east-1.rds.amazonaws.com'
	DATABASE_PORT = ''
	
	GMAPKEY = 'ABQIAAAAKkJhGIDc65pxzIU9FTCsAxTERECPkD_G2wCmHEPQuxrvMkpqRRS1zBq8SdWHxV6_Yp6aTKRlbKk31Q'
	
	PATHTOKEYS = '/home/django/domains/hisg.org/hisg/keys/'
	PATHTOSFPJS = 'http://profile.hisg.org/site_media/sfp/sfp_widget.js'
	PATHTOSFP = 'http://profile.hisg.org/'
	SITESERVER = 'HISG'
	
	XMLRPCIP = 'http://profile.hisg.org/RPC2'

else:
	DEBUG = True
	TEMPLATE_DEBUG = DEBUG
	DATABASE_ENGINE = ''		   # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
	DATABASE_NAME = ''			 # Or path to database file if using sqlite3.
	DATABASE_USER = ''			 # Not used with sqlite3.
	DATABASE_PASSWORD = ''		 # Not used with sqlite3.
	DATABASE_HOST = ''			 # Set to empty string for localhost. Not used with sqlite3.
	DATABASE_PORT = ''			 # Set to empty string for default. Not used with sqlite3.
	# Absolute path to the directory that holds media.
	# Example: "/home/media/media.lawrence.com/"
	MEDIA_ROOT = ''
	# URL that handles the media served from MEDIA_ROOT. Make sure to use a
	# trailing slash if there is a path component (optional in other cases).
	# Examples: "http://media.lawrence.com", "http://example.com/media/"
	MEDIA_URL = ''
	# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
	# trailing slash.
	# Examples: "http://foo.com/media/", "/media/".
	ADMIN_MEDIA_PREFIX = '/admin_media/'
	TEMPLATE_DIRS = (
		# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
		# Always use forward slashes, even on Windows.
		# Don't forget to use absolute paths, not relative paths.
	)





# DEBUG = False
# TEMPLATE_DEBUG = DEBUG
SITE_UP =True # This is for maintainence mode.

ADMINS = (
	# ('tanderson', 'tanderson@hisg.org'),
)

MANAGERS = ADMINS

# DATABASE_ENGINE = 'mysql'	# 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
# DATABASE_NAME = 'hisg_org'	   # Or path to database file if using sqlite3.
# DATABASE_USER = 'hisg_org_admin'			 # Not used with sqlite3.
# DATABASE_PASSWORD = 'Qrt63Lm0Zp'		 # Not used with sqlite3.
# DATABASE_HOST = '10.3.20.12'			 # Set to empty string for localhost. Not used with sqlite3.
# DATABASE_PORT = ''			 # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://www.postgresql.org/docs/8.1/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
# although not all variations may be possible on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'US/Eastern'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"

# import os.path

#MEDIA_ROOT = os.path.join(os.path.dirname(__file__), "site_media")
# MEDIA_ROOT = "/home/django/domains/hisg.org/media/site_media/"

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
# MEDIA_URL = '/site_media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
# ADMIN_MEDIA_PREFIX = '/admin_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'bk-e2zv3humar79nm=j*bwc=-ymeit(8a20whp3goq4dh71t)s'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.load_template_source',
	'django.template.loaders.app_directories.load_template_source',
	# 'dbtemplates.loader.load_template_source',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	# 'account.middleware.LocaleMiddleware',
	'django.middleware.doc.XViewMiddleware',
	'pagination.middleware.PaginationMiddleware',
	# 'misc.middleware.SortOrderMiddleware',
	'django.middleware.transaction.TransactionMiddleware',
	'pages.middleware.PageFallbackMiddleware',
)

ROOT_URLCONF = 'hisg.urls'

# import os.path

# TEMPLATE_DIRS = (
# 	os.path.join(os.path.dirname(__file__), "templates"),
# )

TEMPLATE_CONTEXT_PROCESSORS = (
	"django.core.context_processors.auth",
	"django.core.context_processors.debug",
	"django.core.context_processors.i18n",
	"django.core.context_processors.media",
	"django.core.context_processors.request",
	"homepage.models.context_navigation",
	# "notification.context_processors.notification",
	# "announcements.context_processors.site_wide_announcements",
	# "account.context_processors.account",
	# "misc.context_processors.contact_email",
	# "misc.context_processors.site_name",
	# "messages.context_processors.inbox",
	# "misc.context_processors.combined_inbox_count",
)

COMBINED_INBOX_COUNT_SOURCES = (
	"messages.context_processors.inbox",
	"notification.context_processors.notification",
)

INSTALLED_APPS = (
	# included
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.humanize',
	'django.contrib.markup',
	# 'tiq_login',
	'clogin',
	'pages',
	
	# external
	# 'emailconfirmation',
	# 'django_extensions',
	'robots',
	'mailer',
	'pagination',
	'gravatar',
	# 'threadedcomments',
	# 'timezones',
	# 'feedutil',
	# 'ajax_validation',
	'photologue',
	'tagging',
	# 'things',
	'newsphotos',
	'chunks',
	'videos',
	'countries',
	'about',
	'homepage',
	'featured',
	'brick',
	'histidr',
	'projectsmodels',
	'faqs',
	'training',
	'hub',
	'newadmin',

	# added these to get the site working in mysql
	# 'account',
	# 'notification',
	# 'messages',
		
	# internal (for now)
	# 'analytics',
	# 'misc',
	'photos',
	'rpc4django',
	
	'django.contrib.admin',

)

ABSOLUTE_URL_OVERRIDES = {
	"auth.user": lambda o: "/profiles/%s/" % o.username,
}

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
AUTHENTICATION_BACKENDS = ('clogin.clogin_backend.CloginBackend',)
AUTH_PROFILE_MODULE = 'clogin.CloginProfile'
# AUTHENTICATION_BACKENDS = ('tiq_login.tiq_backend.TiqLoginBackend',)
# AUTH_PROFILE_MODULE = 'tiq_login.TiqUserProfile'
# AUTH_PROFILE_MODULE = 'profiles.Profile'
# NOTIFICATION_LANGUAGE_MODULE = 'account.Account'

EMAIL_CONFIRMATION_DAYS = 2
EMAIL_DEBUG = DEBUG
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = 'contact@hisg.org'
EMAIL_HOST_PASSWORD = '45terKs82'
CONTACT_EMAIL = "contact@hisg.org"
# EMAIL_HOST = "smtp.gmail.com"
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'hisg.contact@gmail.com'
# EMAIL_HOST_PASSWORD = '1qaz2wsx'
# CONTACT_EMAIL = "hisg.contact@gmail.com"
EMAIL_USE_TLS = True


SITE_NAME = "HISG"
LOGIN_URL = "/login/popup"
LOGIN_REDIRECT_URL = "/"
# LOGIN_REDIRECT_URLNAME = "what_next"

LOGGING_OUTPUT_ENABLED = True
LOGGING_SHOW_METRICS = True
LOGGING_LOG_SQL = True

INTERNAL_IPS = (
	'127.0.0.1',
)

ugettext = lambda s: s
LANGUAGES = (
  ('en', u'English'),
  ('de', u'Deutsch'),
  ('es', u'Español'),
  ('fr', u'Français'),
  ('sv', u'Svenska'),
  ('pt-br', u'Português brasileiro'),
  ('he', u'עברית'),
  ('ar', u'العربية'),
  ('it', u'Italiano'),
)

# URCHIN_ID = "ua-..."

CACHE_BACKEND = "locmem:///?max_entries=3000"
FEEDUTIL_SUMMARY_LEN = 60*7 # 7 hours

class NullStream(object):
	def write(*args, **kw):
		pass
	writeline = write
	writelines = write

RESTRUCTUREDTEXT_FILTER_SETTINGS = { 'cloak_email_addresses': True,
									 'file_insertion_enabled': False,
									 'raw_enabled': False,
									 'warning_stream': NullStream(),
									 'strip_comments': True,}

# if Django is running behind a proxy, we need to do things like use
# HTTP_X_FORWARDED_FOR instead of REMOTE_ADDR. This setting is used
# to inform apps of this fact
BEHIND_PROXY = False

FORCE_LOWERCASE_TAGS = True

# WIKI_REQUIRES_LOGIN = True

# GMAPKEY = 'ABQIAAAAKkJhGIDc65pxzIU9FTCsAxTERECPkD_G2wCmHEPQuxrvMkpqRRS1zBq8SdWHxV6_Yp6aTKRlbKk31Q'

# local_settings.py can be used to override environment-specific settings
# like database and email that differ between development and production.
# try:
# 	from local_settings import *
# except ImportError:
# 	pass



# HAYSTACK_SEARCH_ENGINE = 'whoosh'
# HAYSTACK_WHOOSH_PATH = '~/symlinks/site-packages'