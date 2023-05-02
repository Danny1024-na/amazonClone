from django.urls import path
from .views import OrderList,add_to_cart,invoice,checkout,remove_to_cart
from .api import CartDetailCreatApi, OrderListApi,CreateOrder

app_name ='orders'

urlpatterns = [
    path('',OrderList.as_view(),name='order_list'),
    path('add-to-cart',add_to_cart,name='add_to_cart'),
    path('remove-to-cart',remove_to_cart,name='remove_to_cart'),
    path('checkout',checkout,name='checkout'),

    path("api/<str:username>/cart", CartDetailCreatApi.as_view(), name=""),
    path("api/<str:username>/orders", OrderListApi.as_view(), name=""),
    path("api/<str:username>/create-order", CreateOrder.as_view(), name="")
]
