#!/bin/bash

set -e

chown -R www-data:www-data /eetvoudig/

cd /usr/src/app/
>&2 echo "Running site with uwsgi"
uwsgi --chdir /usr/src/app \
    --socket :8000 \
    --socket-timeout 1800 \
    --uid 33 \
    --gid 33 \
    --threads 5 \
    --processes 5 \
    --module eetvoudig.wsgi:application \
    --harakiri 1800 \
    --master \
    --max-requests 5000 \
    --vacuum \
    --limit-post 0 \
    --post-buffering 16384 \
    --thunder-lock \
    --logto '/eetvoudig/log/uwsgi.log'