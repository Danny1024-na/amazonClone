from django.shortcuts import render,redirect
from django.views.generic import ListView,View
from .models import Order,Cart,Cartdetail,Coupon,Orderdetail
from product.models import Product
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.http import JsonResponse
from django.template.loader import render_to_string

import stripe
from django.conf import settings

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

def remove_from_Cart(request,id):
    cart_detail = Cartdetail.objects.get(id=id)
    cart_detail.delete()
    return redirect('/products')

def checkout(request):
    cart = Cart.objects.get(user=request.user , orderStatus = 'Inprogress')
    cart_detail = Cartdetail.objects.filter(cart=cart)
    discount = 0
    delivery_fee = 50
    total = delivery_fee + cart.cart_total()
    sub_total = cart.cart_total()
    
    if request.method == 'POST':
        code = request.POST['coupon']
        coupon = get_object_or_404(Coupon , code=code)
        today_date = datetime.today().date()
        
        if coupon and coupon.quantity > 0 :
            if today_date >= coupon.from_date and today_date <= coupon.to_date:
                code_value = cart.cart_total() / 100 * coupon.value
                discount = round(code_value,2)
                total = cart.cart_total() - code_value
                total = total + delivery_fee
                
                html = render_to_string('include/checkout_table.html',{'cart':cart ,'cart_detail':cart_detail,'delivery_fee':delivery_fee,'total':total,'sub_total':sub_total,'discount':discount })
                return JsonResponse({'result':html})
        
    return render(request,'orders/checkout.html',{'cart':cart ,'cart_detail':cart_detail,'delivery_fee':delivery_fee,'total':total,'sub_total':sub_total,'discount':discount })


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        # Get the amount from the POST data
        amount = request.POST.get('amount')
        stripe.api_key = 'sk_test_51NIAGNFMiQiar3e2N1QJ0dTs0sXjx8Uyer8I8cYmv3WS6Q5lRAxsurSKA6E0Rn4xHYQdzOTlRT7WTpboiw8mxEy100hWVxuTn4'
        # Create a new Checkout session
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': amount,
                    'product_data': {
                        'name': 'Your Product Name',
                    },
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://127.0.0.1:8000/orders/payment/success',
            cancel_url='http://127.0.0.1:8000/orders/payment/fail',
        )

        # Return the session ID as a JSON response
        return JsonResponse({'sessionId': session.id})

def payment_success(request):
    cart = Cart.objects.get(user=request.user , orderStatus = 'Inprogress')
    cart_detail = Cartdetail.objects.filter(cart=cart)
    
    new_order = Order.objects.create(user = request.user)
    for item in cart_detail:
        Orderdetail.objects.create(
            order = new_order , 
            product = item.product , 
            price = item.price , 
            quantity = item.quantity , 
            total = item.total
        )
        
    cart.orderStatus = 'Completed'
    cart.save()
    return redirect('/')

def payment_fail(request):
    pass