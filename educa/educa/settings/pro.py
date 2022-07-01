from .base import *
DEBUG = True
ADMINS = (
     ('Antonio M', 'basicprof@gmail.com'),
)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cours$cours',
        'USER': 'cours',
        'PASSWORD': 'bdpassword',
        'HOST': 'cours.mysql.pythonanywhere-services.com',
        'TEST': {
          'NAME': 'cours$test_cours',
          }
    }
}
ALLOWED_HOSTS = ["*",'cours.pythonanywhere.com',]
 