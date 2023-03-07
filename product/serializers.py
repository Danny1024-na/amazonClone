from .models import Product,Brand,Images,Reviews
from rest_framework import serializers
from django.db.models.aggregates import Avg




class ProductReviewSerilaizer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model =Reviews
        exclude=[]
        fields=['user','comment','rate','created_at']


class ProductImgSerilaizer(serializers.ModelSerializer):
    class Meta:
        model =Images
        exclude=[]
        fields=['img']


class ProductListSerializer(serializers.ModelSerializer):
    brand =serializers.StringRelatedField() #the brand cloumen in class Product
    price_with_tax = serializers.SerializerMethodField(method_name='myfunc')
    avg= serializers.SerializerMethodField(method_name='avg_rate')
    review_count =  serializers.SerializerMethodField()

    class Meta:
        model = Product
        exclude = []
        fileds = '__all__'

    def myfunc(self,Product):
        return Product.price*1.1
    
    def avg_rate(self,Product):
       avg= Product.product_review.aggregate(rate_Avg=Avg('rate'))
       avg_rate=avg['rate_Avg']
       if avg_rate :
           return round(avg_rate,2)
       return 0
    
    def get_review_count(self,Product):
        return Product.product_review.all().count()

    
class ProductDetailSerializer(serializers.ModelSerializer):
    brand =serializers.StringRelatedField() #the brand cloumen in class Product
    img = ProductImgSerilaizer(source='product_image',many=True)
    avg= serializers.SerializerMethodField(method_name='avg_rate')
    review_count =  serializers.SerializerMethodField()
    reviews = ProductReviewSerilaizer(source='product_review',many=True)

    class Meta:
        model = Product
        exclude = []
        fileds = '__all__'

    def avg_rate(self,Product):
       avg= Product.product_review.aggregate(rate_Avg=Avg('rate'))
       avg_rate=avg['rate_Avg']
       if avg_rate :
           return round(avg_rate,2)
       return 0
    
    def get_review_count(self,Product):
        return Product.product_review.all().count()

    
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

