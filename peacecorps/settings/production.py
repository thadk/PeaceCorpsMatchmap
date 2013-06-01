import os
import dj_database_url

from common import *

DEBUG = False
TEMPLATE_DEBUG = False
DEBUG_SQL = False


DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}
