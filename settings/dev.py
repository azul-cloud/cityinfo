from .base import *

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'cityinfo',                      # Or path to database file if using sqlite3.
            'USER': 'admin',
            'PASSWORD': 'student12',
            'HOST': 'localhost',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
            'PORT': '',                      # Set to empty string for default.
            'TEST_NAME': 'cityinfo_test',
        }
    }

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

DEBUG = True
TEMPLATE_DEBUG = True