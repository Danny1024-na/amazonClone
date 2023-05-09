from django.shortcuts import render ,redirect
from .models import Profile,Address,ContactNumbers
from .forms import Activate,SignUpForm
from django.core.mail import send_mail
from django.contrib.auth.models import User
from product.models import Product,Brand,Reviews
from orders.models import Order
# Create your views here.

def signUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            #to get the needed data form the dic in a form ,muss nach is valid sein , denn es valid sein muss
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            form.save()

            profile =Profile.objects.get(user__username=username) # tow under score :go to Profile class dann column user and get the table of the User(Fremd key)

            send_mail(
                    "Actiavate ur account",
                    f"Welcome {username} \n use this code {profile.code} to actiavte ur account... \n Green-Sotre",
                    "danina964@gmail.com",
                    [email],
                    fail_silently=False,
                    )
        return redirect(f'/accounts/{username}/activate')
    else:
        form = SignUpForm()
        
    return render(request,'accounts/signUp.html',{'form':form})

def activate(request,username):
    profile= Profile.objects.get(user__username=username)
    if request.method == 'POST':
        form =Activate(request.POST)
        if form.is_valid():
            code =form.cleaned_data['code']
            if code == profile.code:
                profile.code =''
                profile.save()
                return redirect('/accounts/login')
    else:
        form =Activate()
    return render(request,'accounts/activate.html',{'form':form})
    

def profile(request):
    profile=Profile.objects.get(user=request.user)
    address=Address.objects.filter(user=request.user)
    contactNumbers=ContactNumbers.objects.filter(user=request.user)
    return render(request,'accounts/profile.html',{'profile':profile,'contactNumbers':contactNumbers,'address':address})

def dashboard(request):
    user =User.objects.all().count()
    product =Product.objects.all().count()
    reviews =Reviews.objects.all().count()
    brands = Brand.objects.all().count()
    orders = Order.objects.all().count()

    recieved = Order.objects.filter(orderStatus='Recieved').count()
    processed = Order.objects.filter(orderStatus='Processed').count()
    delivered = Order.objects.filter(orderStatus='Delivered').count()
    shipped = Order.objects.filter(orderStatus='Shipped').count()

    return render(request,'accounts\dashboard.html',{
        'user':user,
        'product':product,
        'reviews':reviews,
        'brands':brands,
        'orders':orders,
        'recieved':recieved,
        'processed':processed,
        'delivered':delivered,
        'shipped':shipped,
    })

from .tasks import send_build_emails

def test_send(request):
    send_build_emails.delay(5)
    return render(request,'test_celery.html',{})