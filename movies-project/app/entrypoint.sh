#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py migrate

exec "$@"

# So, we referenced the Postgres container using the name of the service, movies-db, which is defined by the SQL_HOST environment variable. The loop continues until something like Connection to movies-db port 5432 [tcp/postgresql] succeeded! is returned.