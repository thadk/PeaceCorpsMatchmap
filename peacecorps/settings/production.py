import os
import dj_database_url

# DJANGO_ENV="PRODUCTION" DJANGO_DEBUG="False"


DEBUG = os.environ.get('DJANGO_DEBUG', "False").lower() == "true"

DEBUG_SQL = False

DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}

ALLOWED_HOSTS = ['peacecorps.herokuapp.com']


###################
# S3 FILE STORAGE #
###################

DEFAULT_FILE_STORAGE = "storages.backends.s3boto.S3BotoStorage"
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", "")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME", "")

AWS_HEADERS = {
    "Cache-Control": "public, max-age=86400",
}

AWS_S3_FILE_OVERWRITE = False
AWS_QUERYSTRING_AUTH = False
AWS_S3_SECURE_URLS = False
AWS_REDUCED_REDUNDANCY = False
AWS_IS_GZIPPED = False

STATIC_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'
MEDIA_URL = STATIC_URL + 'media/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'grappelli/'


#####################
# SENDGRID SETTINGS #
#####################

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = os.environ.get('SENDGRID_USERNAME', "")
EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD', "")
EMAIL_PORT = 587        # 25, 587, 2525 and 465 on ssl
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'thadknull@gmail.com'