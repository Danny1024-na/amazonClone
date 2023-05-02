from .models import Cart, Cartdetail

def get_or_create_cart(request):
    if request.user.is_authenticated: # if the user is looged in
        cart ,created = Cart.objects.get_or_create(user=request.user , orderStatus = 'Inprogress')
        if not created :
            cart_detail =Cartdetail.objects.filter(cart=cart)
            return {'cart':cart, 'cart_detail':cart_detail}
        return {'cart':cart}
    return {}