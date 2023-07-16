from .base import *

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gasession',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': 'db',
        'PORT': '3306',
    }
}