release: python manage.py migrate --no-input
web: gunicorn config.wsgi
worker: celery -A config worker
worker: celery -A config beat --scheduler django_celery_beat.schedulers:DatabaseScheduler