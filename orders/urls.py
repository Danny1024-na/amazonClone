from django.urls import path
from .views import *
from .api import CartDetailCreatApi, OrderListApi,CreateOrder

app_name ='orders'

urlpatterns = [
    path('',OrderList.as_view(),name='order_list'),
    path('add-to-cart',add_to_cart,name='add_to_cart'),
    path('remove-from-cart/<int:id>' , remove_from_Cart , name='remove_from_Cart'),
    path('remove-to-cart/<int:id>',remove_to_cart,name='remove_to_cart'),
    path('checkout',checkout,name='checkout'),
    path('payment/success' , payment_success , name='payment_success'),
    path('payment/fail' , payment_fail , name='payment_fail'),
    path('create_checkout_session/', CreateCheckoutSessionView.as_view(), name='create_checkout_session'),

    #api
    path("api/<str:username>/cart", CartDetailCreatApi.as_view(), name=""),
    path("api/<str:username>/orders", OrderListApi.as_view(), name=""),
    path("api/<str:username>/create-order", CreateOrder.as_view(), name="")
]
