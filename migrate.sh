#!/bin/bash

SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"telesphore@africanoasis.org"}
cd /app/

/opt/venv/bin/python manage.py migrate --noinput
/opt/venv/bin/python manage.py createsuperuser --email $SUPERUSER_EMAIL --noinput || true