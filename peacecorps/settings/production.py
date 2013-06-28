import os
import dj_database_url

DEBUG = os.environ.get('DJANGO_DEBUG', "False").lower() == "true"

DEBUG_SQL = False

DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}

ALLOWED_HOSTS = ['peacecorps.herokuapp.com']


#####################
# SENDGRID SETTINGS #
#####################

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = os.environ['SENDGRID_USERNAME']
EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']
EMAIL_PORT = 587        # 25, 587, 2525 and 465 on ssl
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'thadknull@gmail.com'