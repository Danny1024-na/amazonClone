from django_filters import rest_framework
from .models import Product

class ProdcutFilter(rest_framework.FilterSet):
    class Meta:
        model = Product
        fields = {
            'name' : ['icontains'],
            'price' : ['lte','gte'],
            'brand' : ['exact'],
            'quantity' : ['range'],
        }