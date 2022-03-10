from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('mail/', views.send_email),
    path('hello/', views.views.say_hello)
]
