from django_filters.rest_framework import FilterSet
from .models import Product


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'collection_id': ['exact'],
            'unit_price': ['gt', 'lt']
        }
