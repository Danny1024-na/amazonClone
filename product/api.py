from .serializers import ProductSerializer
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics


@api_view(['GET'])
def productlist_api(request):
    # many = True id we return a list
    #context={"request": request} , make the api return the path of an img as a link and not just a path
    data= ProductSerializer(Product.objects.all(),many=True,context={"request": request}).data
    return Response({'data':data})


class ProductListApi(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDetailApi(generics.RetrieveUpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field='slug'