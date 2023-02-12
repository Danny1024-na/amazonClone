from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product,Brand
from django.db.models import Count
# Create your views here.

class ProductList(ListView):
    model = Product

class ProductDetail(DetailView):
    model = Product

class BrandList(ListView):
    model = Brand
    # give me the number of relations between product and brand
    queryset=Brand.objects.all().annotate(prod_count=Count('product_brand')) # data zurück [:1] return nur erste Brand

class BrandDetail(DetailView):
    model = Brand