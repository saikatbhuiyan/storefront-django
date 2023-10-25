from django.urls import path

from .views import MovieList, MovieDetail


urlpatterns = [
    path("api/movies/", MovieList.as_view()),
    path("api/movies/<int:pk>/", MovieDetail.as_view()),
]
