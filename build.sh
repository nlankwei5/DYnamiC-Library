#!/usr/bin/env bash

# Exit on error
set -o errexit

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate

if [[ $CREATE_SUPERUSER ]];
then
  python manage.py createsuperuser --no-input
fi

