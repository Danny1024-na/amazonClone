from django.urls import path
from .views import OrderList
from .api import CartDetailCreatApi, OrderListApi,CreateOrder

app_name ='orders'

urlpatterns = [
    path('',OrderList.as_view(),name='order_list'),

    path("api/<str:username>/cart", CartDetailCreatApi.as_view(), name=""),
    path("api/<str:username>/orders", OrderListApi.as_view(), name=""),
    path("api/<str:username>/create-order", CreateOrder.as_view(), name="")

]
