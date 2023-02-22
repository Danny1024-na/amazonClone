from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product,Brand
from django.db.models import Count,Q,F,Func,Value,ExpressionWrapper,DecimalField,FloatField
from django.db.models.aggregates import Avg,Min,Max,Count
from django.db.models.functions import Concat
# Create your views here.

def query_debug(request):
    #data=Product.objects.filter(name__contains='michael ',price__gt=30)
    #data=Product.objects.filter(Q(name__contains='michael') | Q (price__gt=30))
    #data=Product.objects.filter(price=F('quantity'))
    #data=Product.objects.all().order_by('-name')
    #data=Product.objects.filter(name__contains='michael ',price__gt=30).order_by('-name')
    #data=Product.objects.only('id','brand')
    #data=Product.objects.select_related('brand').all()
    
    #data = Product.objects.aggregate(price_avg=Avg('price'),price_max=Max('price'))
    #data =Product.objects.annotate(the_new_col=F('quantity')*2)

    #data =Product.objects.annotate(new_name=Func(F('name'),F('quantity'),function='CONCAT'))
    # data =Product.objects.annotate(
    #     new_col=Concat('name',Value(' '),'flag')
    #     )

    data2=Product.objects.annotate(
        new_col=ExpressionWrapper(F('price')*0.8 , output_field=FloatField())
    )
    data=data2.aggregate(name=Max('new_col'))


    return render(request,'product\productlist.html',{'data':data})


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
    template_name="product\\brand_detail.html"

    def get_queryset(self):
        brand =Brand.objects.get(slug=self.kwargs['slug'])
        queryset=Product.objects.filter(brand=brand)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.filter(slug=self.kwargs['slug']).annotate(prod_count=Count('product_brand'))[0] #the slug from the last methode
        return context
    