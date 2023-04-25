#!/bin/sh
python manage.py collectstatic --no-input
python manage.py migrate --force
gunicorn core.wsgi:application --bind 0.0.0.0:8000 --reload