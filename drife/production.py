from drife.common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'drife',
        'USER': 'drife',
        'PASSWORD': 'drife',
        'HOST': 'localhost',
        'PORT': '',
    }
}

WSGI_APPLICATION = 'drife.wsgi_production.application'
DEBUG = False