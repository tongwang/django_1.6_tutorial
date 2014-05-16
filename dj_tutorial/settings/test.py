from dj_tutorial.settings.common import *

PROJECT_APPS = [
    'dj_tutorial.apps.polls',
]

DATABASES = {
    "default": {
        "ENGINE": 'django.db.backends.sqlite3',
    }
}
