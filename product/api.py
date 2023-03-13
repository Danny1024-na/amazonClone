from .serializers import ProductListSerializer,ProductDetailSerializer,BrandDetailSerializer, BrandListSerializer
from .models import Product,Brand
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .pagination import ResultsSetPagination
from django_filters.rest_framework import DjangoFilterBackend
from .myFilter import ProdcutFilter


@api_view(['GET'])
def productlist_api(request):
    # many = True id we return a list
    #context={"request": request} , make the api return the path of an img as a link and not just a path
    data= ProductListSerializer(Product.objects.all(),many=True,context={"request": request}).data
    return Response({'data':data})


class ProductListApi(generics.ListCreateAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()
    pagination_class = ResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name','brand','price','flag']
    filterset_class = ProdcutFilter


class ProductDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()
    lookup_field='slug'


class BrandListApi(generics.ListAPIView):
    serializer_class = BrandListSerializer
    queryset = Brand.objects.all()


class BrnadDetailApi(generics.RetrieveAPIView):
    serializer_class = BrandDetailSerializer
    queryset = Brand.objects.all()
    lookup_field='slug'