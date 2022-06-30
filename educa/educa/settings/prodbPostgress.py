from .base import *
DEBUG = True
ADMINS = (
     ('Antonio M', 'basicprof@gmail.com'),
)
# ALLOWED_HOSTS = ['educaproject.com', 'www.educaproject.com']
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
ALLOWED_HOSTS = ['127.0.0.1','educaproject.com', 'www.educaproject.com']