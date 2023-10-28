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

## Architecture

[Django REST Framework](https://www.django-rest-framework.org/) (DRF) is a widely-used, full-featured API framework designed for building RESTful APIs. If you need to build a RESTful API with Django, it's the package to use.

DRF is composed of the following components:

1. [Serializers](https://www.django-rest-framework.org/api-guide/serializers/) are used to convert Django querysets and model instances to (serialization) and from (deserialization) JSON (and a number of other data rendering formats like XML and YAML).
2. [Views](https://www.django-rest-framework.org/api-guide/views/) (along with [ViewSets](https://www.django-rest-framework.org/api-guide/viewsets/)), which are similar to traditional Django views, handle HTTP requests and return the serialized data. The view itself uses the serializers to validate incoming payloads and contains the necessary logic to return the response. Views are coupled with [routers](https://www.django-rest-framework.org/api-guide/routers/), which map the views back to the exposed URLs.

### View

Like traditional Django views, DRF views are Python functions or classes that take HTTP requests and return HTTP responses.

DRF has three types of views:

1. [Views](https://testdriven.io/blog/drf-views-part-1/), which subclasses Django's `View` class, are the most basic (and most explicit) DRF view type. They can be function (implemented via the `api_view` decorator) or class (implemented via the `APIView` class) based.
2. [ViewSets](https://testdriven.io/blog/drf-views-part-3/) provide a layer of abstraction above DRF views. They are often used to combine the create, read, update, and destroy (CRUD) logic into a single view. A ViewSet "helps ensure that URL conventions will be consistent across your API, minimizes the amount of code you need to write, and allows you to concentrate on the interactions and representations your API provides rather than the specifics of the URL conf". They are perfect for implementing the basic CRUD operations for your API. They can be limiting though if your API goes beyond the basics or the API endpoints don't cleanly map back to the models.
3. [Generic Views](https://testdriven.io/blog/drf-views-part-2/) typically take the abstraction further by inferring the response format, allowed methods, and payload shape based on the serializer.

> We'll be using the `APIView` class view in this course. Feel free to check your understanding by implementing your API with a different type of view.



```
$ docker-compose exec movies python manage.py flush
$ docker-compose exec movies python manage.py loaddata movies.json
```
