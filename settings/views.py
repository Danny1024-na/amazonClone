from django.shortcuts import render
from django.db.models import Count
from product.views import Brand,Product,Reviews

# Create your views here.
def home(request):
    brand=Brand.objects.all().annotate(prod_count=Count('product_brand'))
    item_sale=Product.objects.filter(flag='Sale')[:10]
    item_feature=Product.objects.filter(flag='Feature')[:6]
    item_new=Product.objects.filter(flag='New')[:12]
    reviews=Reviews.objects.all()[:6]
    return render(request,'settings/home.html',{
        'brands':brand ,
        'items_sale':item_sale,
        'item_feature' : item_feature,
        'items_new':item_new,
        'reviews' : reviews,
        })