import os

DEBUG = os.environ.get('DJANGO_DEBUG', "True").lower() == "true"

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
       'NAME': 'sqlite.db',                      # Or path to database file if using sqlite3.
       'USER': '',                      # Not used with sqlite3.
       'PASSWORD': '',                  # Not used with sqlite3.
       'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
       'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
   }
}

STATIC_ROOT= ''

MEDIA_ROOT = "media"
MEDIA_URL = "http://localhost:8000/media/"

ALLOWED_HOSTS = ['*']

try:
    from localenv import *
except ImportError:
    pass # No overrides specified
