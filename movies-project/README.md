```
docker-compose exec movies python manage.py migrate --noinput
```

```
docker-compose exec movies-db psql --username=movies --dbname=movies_dev
```

docker volume inspect movies-project_postgres_data

```
docker-compose up -d --build
```

```
docker-compose exec movies pytest
```


```
docker-compose exec movies python manage.py makemigrations
```


```
docker-compose exec movies python manage.py migrate
```
