import dj_database_url
import django_heroku

from .base import *

DEBUG = bool(int(os.getenv("DEBUG", False)))

ALLOWED_HOSTS = os.getenv("ALLOWED_HOST", "").split(" ")

INSTALLED_APPS += [

]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
    }
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# 정적파일의 크기를 줄여서 서빙
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Heroku 관련 설정들
django_heroku.settings(locals())

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
