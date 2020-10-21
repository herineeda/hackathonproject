from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS += [

]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(ROOT_DIR, 'db.sqlite3'),
    }
}
