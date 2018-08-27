#!/bin/bash

python manage.py collectstatic --clear --no-input
python manage.py migrate

if  [[ $RUN_TYPE == "production" ]]; then
uwsgi --wsgi-file test.py
    uwsgi --socket :8001  --module oauth2_server.wsgi --master --processes 10;
else
    python manage.py runserver 0.0.0.0:8001;
fi
