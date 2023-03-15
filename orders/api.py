from .models import Cart,Order,Orderdetail,Cartdetail
from product.models import Product
from rest_framework.decorators import api_view
from rest_framework import generics
from .serlializers import Cartserializer,CartDetailSerializer,OrderDetailSerializer,OrderSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User


class OrderListApi(generics.GenericAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    # we have to write def list , but by me don't run 'get not allowed' therefor i have worte def get
    def get(self,request,*args,**kwargs):
        user = User.objects.get(username= self.kwargs['username'])
        queryset = self.get_queryset().filter(user=user)
        serializer = OrderSerializer(queryset,many=True)
        return Response(serializer.data)
    

class CreateOrder(generics.GenericAPIView):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(username= self.kwargs['username']) 
        cart = Cart.objects.get(user=user, orderStatus='Inprogress')
        cart_data =Cartdetail.objects.filter(cart=cart)

        new_order = Order.objects.create(user=user)
        for object in cart_data:
            Orderdetail.objects.create(
                order = new_order,
                product =object.product,
                price =object.price,
                quantitiy = object.quantitiy,
                total = object.total
            )
        cart.orderStatus='Completed'
        cart.save()
        return Response({'status':200})

class CartDetailCreatApi(generics.GenericAPIView): # kann man list oder detail hier bei generic nutzen
    serializer_class= CartDetailSerializer

    def get(self,request,*args,**kwargs):
        user = User.objects.get(username= self.kwargs['username']) # kwargs : get username form the link 
        cart ,created= Cart.objects.get_or_create(user=user, orderStatus='Inprogress') # return the cart if it exist and craeate a new empty one if not 
        data = Cartserializer(cart).data
        return Response({'cart':data})
        
    def post(self,request,*args,**kwargs):
        user = User.objects.get(username=self.kwargs['username'])

        product = Product.objects.get(id= request.data['product_id'])
        quantity = request.data['quantity']

        cart = Cart.objects.get(user=user , orderStatus='Inprogress')
        cart_data,created =Cartdetail.objects.get_or_create(cart=cart,product=product)
        cart_data.price = product.price
        cart_data.quantitiy=quantity
        cart_data.total= round(cart_data.price*cart_data.quantitiy,2)
        cart_data.save()
        return Response({'status':200})
    
    def delete(self,request,*args,**kwargs):
        user = User.objects.get(username=self.kwargs['username'])

        product = Product.objects.get(id= request.data['product_id'])
        cart = Cart.objects.get(user=user , orderStatus='Inprogress')
        Cartdetail.objects.get(cart=cart,product=product).delete()
        return Response({'status':200 , 'message' : 'deletes successfully'})

