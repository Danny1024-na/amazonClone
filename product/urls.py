from django.urls import path
from .views import ProductList,ProductDetail,BrandList,BrandDetail,query_debug,addReview

app_name = 'product'

urlpatterns = [
    path('debug' , query_debug ,name='query_debug'),

    path('' , ProductList.as_view() ,name='product_list'),
    path('<slug:slug>', ProductDetail.as_view() ,name='product_detail'), 

    path('<slug:slug>/addReview', addReview ,name='addReview'), 

    path('brands/', BrandList.as_view(),name='brand_list'),
    path('brands/<slug:slug>', BrandDetail.as_view() ,name='brand_detail'),
]
