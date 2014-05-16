from dj_tutorial.settings.common import *

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tutorial',
        'USER': 'root',
        'STORAGE_ENGINE': 'INNODB',
    }
}
