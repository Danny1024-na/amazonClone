from rest_framework import serializers
from .models import Cart,Cartdetail,Order,Orderdetail


class CartDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartdetail
        exclude=['cart']


class Cartserializer(serializers.ModelSerializer):
    cart_detail=CartDetailSerializer(many=True)

    class Meta:
        model = Cart
        fields ='__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orderdetail
        fields ='__all__'

class OrderSerializer(serializers.ModelSerializer):
    order_detail = OrderDetailSerializer(many=True)

    class Meta:
        model = Order
        exclude = ['user']