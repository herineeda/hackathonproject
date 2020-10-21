release: python manage.py migrate --settings="ddingproject.settings.prod"
web: gunicorn ddingproject.wsgi --log-file -