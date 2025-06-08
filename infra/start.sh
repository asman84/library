#!/bin/bash
set -e

# Load base data
pip install -r requirements.txt
python manage.py makemigrations --noinput
python manage.py migrate --noinput

#celery -A _project_ worker -B -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler &

if [[ $DJANGO_DEBUG -eq 0 ]]; then
  # production mode
  echo "production mode"
  python manage.py collectstatic --noinput
  gunicorn -w 4 --env DJANGO_SETTINGS_MODULE=upwork1.settings upwork1.wsgi -b 0.0.0.0:8000
else
  echo "development mode"
  python manage.py runserver 0.0.0.0:8000
fi
