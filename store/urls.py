from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('products/', views.product_list),
]
