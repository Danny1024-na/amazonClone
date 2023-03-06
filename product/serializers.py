from .models import Product,Brand
from rest_framework import serializers


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model= Brand
        exclude =[]
        fields = ['name']


class ProductSerializer(serializers.ModelSerializer):
    brand =BrandSerializer() #the brand cloumen in class Produc
    price_with_tax = serializers.SerializerMethodField(method_name='myfunc')

    class Meta:
        model = Product
        exclude = []
        fileds = '__all__'

    def myfunc(self,Product):
        return Product.price*1.1