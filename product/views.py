from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product,Brand
from django.db.models import Count
# Create your views here.

class ProductList(ListView):
    model = Product
    paginate_by=50

class ProductDetail(DetailView):
    model = Product

class BrandList(ListView):
    model = Brand
    paginate_by =50
    queryset=Brand.objects.all().annotate(prod_count=Count('product_brand')) # data zurück [:1] return nur erste Brand

class BrandDetail(ListView):
    model = Product ### Achtuuuunnnnggggg!!!!
    paginate_by =50

    def get_queryset(self):
        brand =Brand.objects.get(slug=self.kwargs['slug'])
        queryset=Product.objects.filter(brand=brand)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.filter(slug=self.kwargs['slug']).annotate(prod_count=Count('product_brand'))[0] #the slug from the last methode
        return context
    