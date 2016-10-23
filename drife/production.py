from drife.common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'drife',
        'USER': 'drife',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

WSGI_APPLICATION = 'drife.wsgi_production.application'