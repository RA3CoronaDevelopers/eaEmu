# Django settings for eaEmu project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
   ('elitak', 'elitak@gmail.com'),
)

MANAGERS = ADMINS

## sqlite3 db
#DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#import os; DATABASE_NAME = os.path.abspath('eaEmu.db')             # Or path to database file if using sqlite3.

## mysql db
DATABASE_ENGINE = 'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'eaEmu'             # Or path to database file if using sqlite3.
DATABASE_USER = 'eaEmu'             # Not used with sqlite3.
DATABASE_PASSWORD = 'HZeLpG2rB825LnFc'         # Not used with sqlite3.
##setup account and listening interfaces before using DATABASE_HOST
#DATABASE_HOST = '192.168.0.113'             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

## Local time zone for this installation. Choices can be found here:
## http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
## although not all choices may be available on all operating systems.
## If running in a Windows environment this must be set to the same as your
## system time zone.
TIME_ZONE = 'America/Los_Angeles'

## Language code for this installation. All choices can be found here:
## http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

## If you set this to False, Django will make some optimizations so as not
## to load the internationalization machinery.
USE_I18N = True

## Absolute path to the directory that holds media.
## Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

## URL that handles the media served from MEDIA_ROOT. Make sure to use a
## trailing slash if there is a path component (optional in other cases).
## Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

## URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
## trailing slash.
## Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

## Make this unique, and don't share it with anybody.
SECRET_KEY = 'd$6xxdqiqys!mjx9=8&1!w-5hi4stq%z(00v#i025*7+9i5d5d'

## List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'djproj.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django_evolution',
    'dj.eaEmu',
)
