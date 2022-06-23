from .base import *
DEBUG = False
ADMINS = (
     ('Antonio M', 'basicprof@gmail.com'),
)
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'rootroot',
        'HOST': '127.0.0.1', 
        'PORT': '5433'
    }
}