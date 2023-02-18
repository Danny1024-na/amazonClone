from django.urls import path
from .views import ProductList,ProductDetail,BrandList,BrandDetail

app_name = 'product'

urlpatterns = [
    path('' , ProductList.as_view() ,name='product_list'),
    path('<slug:slug>', ProductDetail.as_view() ,name='product_detail'),  
    path('brands/', BrandList.as_view(),name='brand_list'),
    path('brands/<slug:slug>', BrandDetail.as_view() ,name='brand_detail'),
]
