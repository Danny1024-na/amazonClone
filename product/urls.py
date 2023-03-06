from django.urls import path
from .views import ProductList,ProductDetail,BrandList,BrandDetail,query_debug,add_review
from .api import productlist_api,ProductListApi,ProductDetailApi,ProductDetailApi, BrandListApi,BrnadDetailApi

app_name = 'product'

urlpatterns = [
    path('debug' , query_debug ,name='query_debug'),

    path('' , ProductList.as_view() ,name='product_list'),
    path('<slug:slug>', ProductDetail.as_view() ,name='product_detail'), 

    path('<slug:slug>/add-review', add_review ,name='add_review'), 

    path('brands/', BrandList.as_view(),name='brand_list'),
    path('brands/<slug:slug>', BrandDetail.as_view() ,name='brand_detail'),

    #api urls
    path ('api/list', productlist_api,name='product list'),
    #or
    #path('api/list', ProductSerializer.as_view() ,name='product list'),

    #beide müssen hier sein ,damit django verstehen kann, dass die Links nicht wie die Links oben
    path('api/list/brands', BrandListApi.as_view() ,name='brand list'),
    path('api/list/brands/<slug:slug>', BrnadDetailApi.as_view() ,name='brand detail'),

    path('api/list/<slug:slug>', ProductDetailApi.as_view() ,name='product detail'),

]


