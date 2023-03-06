from .models import Product,Brand,Images
from rest_framework import serializers



class ProductImgSerilaizer(serializers.ModelSerializer):
    class Meta:
        model =Images
        exclude=[]
        fields=['img']


class ProductListSerializer(serializers.ModelSerializer):
    brand =serializers.StringRelatedField() #the brand cloumen in class Product
    price_with_tax = serializers.SerializerMethodField(method_name='myfunc')
    avg= serializers.SerializerMethodField(method_name='avg_rate')

    class Meta:
        model = Product
        exclude = []
        fileds = '__all__'

    def myfunc(self,Product):
        return Product.price*1.1
    
    def avg_rate(self,Product):
        return Product.get_avg_rate()
    
class ProductDetailSerializer(serializers.ModelSerializer):
    brand =serializers.StringRelatedField() #the brand cloumen in class Product
    img = ProductImgSerilaizer(source='product_image',many=True)

    class Meta:
        model = Product
        exclude = []
        fileds = '__all__'
    
class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model= Brand
        exclude =[]
        fields = '__all__'

class BrandDetailSerializer(serializers.ModelSerializer):
    products= ProductListSerializer(source='product_brand',many=True)

    class Meta:
        model= Brand
        exclude =[]
        fields = '__all__'

