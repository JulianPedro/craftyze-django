#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."
    while ! nc -z "$SQL_HOST" "$SQL_PORT"; do
      sleep 0.1
    done
    echo "PostgreSQL started"
fi

python manage.py migrate --fake-initial
python manage.py collectstatic --noinput
#python manage.py makemessages -l en -l pt_BR
python manage.py compilemessages
#python manage.py compress --force

exec "$@"
