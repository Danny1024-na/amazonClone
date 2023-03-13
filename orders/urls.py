from django.urls import path
from .views import OrderList
from .api import CartDetailCreatApi

app_name ='orders'

urlpatterns = [
    path('',OrderList.as_view(),name='order_list'),

    path("api/<str:username>/cart", CartDetailCreatApi.as_view(), name="")
]
