#!/bin/bash

set -e

echo "${0}: running migrations."
python manage.py makemigrations --merge
python manage.py migrate --noinput

echo "${0}: collecting statics."

python manage.py collectstatic --noinput

if [ ! -d "backend/static_shared" ]; then
    mkdir backend/static_shared
fi

cp -rv backend/static/* backend/static_shared/

gunicorn backend.asgi:application -k uvicorn.workers.UvicornWorker \
    --env DJANGO_SETTINGS_MODULE=backend.settings \
    --name backend \
    --bind 0.0.0.0:8000 \
    --timeout 600 \
    --workers 2 \
    --log-level=info \
    --reload