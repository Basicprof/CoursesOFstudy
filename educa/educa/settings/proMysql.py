from .base import *
DEBUG = True
ADMINS = (
     ('Antonio M', 'basicprof@gmail.com'),
)
# ALLOWED_HOSTS = ['educaproject.com', 'www.educaproject.com']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'coursesall$coursesdb',
        'USER': 'coursesall',
        'PASSWORD': 'CreateDb',
        'HOST': 'coursesall.mysql.pythonanywhere-services.com',
        'TEST': {
          'NAME': 'coursesall$test_coursesdb',
          }
    }
}
ALLOWED_HOSTS = ['coursesall.pythonanywhere.com',]
 