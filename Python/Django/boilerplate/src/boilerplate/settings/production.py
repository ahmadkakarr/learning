from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['ip-address', 'www.your-website.com']


# Application definition

INSTALLED_APPS += [
    
]

MIDDLEWARE += [
    
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'your-db-name',
        'USER': 'your-db-user-name',
        'PASSWORD': 'your-db-password',
        'HOST': 'localhost',
        'PORT': ''
    }
}


STRIPE_PUBLIC_KEY = 'your-live-public-key'
STRIPE_PUBLIC_KEY = 'your-live-secret-key'