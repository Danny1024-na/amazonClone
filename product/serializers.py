from .models import Product,Brand
from rest_framework import serializers


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model= Brand
        exclude =[]
        fields = ['name']


class ProductSerializer(serializers.ModelSerializer):
    brand =BrandSerializer() #the brand cloumen in class Product

    class Meta:
        model = Product
        exclude = []
        fileds = '__all__'