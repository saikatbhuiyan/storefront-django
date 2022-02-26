from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet)

products_router = routers.NestedDefaultRouter(
    router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet,
                         basename='product-reviews')


# URLConf
urlpatterns = router.urls + products_router.urls

# urlpatterns = [
#     path('products/', router.urls),
#     path('products/', views.ProductList.as_view()),
#     path('products/<int:pk>/', views.ProductDetail.as_view()),
#     path('collections/', views.collection_list),
#     path('collections/<int:pk>/', views.collection_detail,
#          name='collection-detail'),
# ]
