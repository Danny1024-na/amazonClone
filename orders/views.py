from django.shortcuts import render,redirect
from django.views.generic import ListView
from .models import Order,Cart,Cartdetail
from product.models import Product

class OrderList(ListView):
    model=Order
    context_object_name ='orders'
    paginate_by =1

def add_to_cart(request):
    quantity = request.POST['quantity'] # request.POST.get('quantity')
    product =Product.objects.get(id=request.POST['product_id'])
    cart = Cart.objects.get(user=request.user, orderStatus='Inprogress')
    cart_detail ,created=Cartdetail.objects.get_or_create(cart=cart, product=product)
    cart_detail.quantitiy=quantity
    cart_detail.price=product.price
    cart_detail.total=round(int(quantity)*product.price)
    cart_detail.save()
    return redirect(f'/products/{product.slug}')

def remove_to_cart(request,id):
    cart_detail= Cartdetail.objects.get(id=id)
    cart_detail.delete()
    return redirect('/products')

def checkout(request):
    cart = Cart.objects.get(user=request.user, orderStatus='Inprogress')
    cart_detail=Cartdetail.objects.filter(cart=cart)

    delivery_fee = 50
    total =delivery_fee + cart.cart_total()
    discount=0
    sub_total =cart.cart_total()
    return render(request,'orders/checkout.html',{'cart':cart , 'cart_detail':cart_detail , 'delivery_fee':delivery_fee , 'total':total ,'sub_total':sub_total , 'discount':discount})

def invoice(request):
    pass