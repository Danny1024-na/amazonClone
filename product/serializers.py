from .models import Product,Brand
from rest_framework import serializers



class ProductSerializer(serializers.ModelSerializer):
    brand =serializers.StringRelatedField() #the brand cloumen in class Produc
    price_with_tax = serializers.SerializerMethodField(method_name='myfunc')

    class Meta:
        model = Product
        exclude = []
        fileds = '__all__'

    def myfunc(self,Product):
        return Product.price*1.1
    
class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model= Brand
        exclude =[]
        fields = '__all__'

class BrandDetailSerializer(serializers.ModelSerializer):
    products= ProductSerializer(source='product_brand',many=True)

    class Meta:
        model= Brand
        exclude =[]
        fields = '__all__'

