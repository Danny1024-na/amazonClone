from django.shortcuts import render
from .models import Profile,Address,ContactNumbers
# Create your views here.

def signUp():
    pass

def activate():
    pass 

def profile(request):
    profile=Profile.objects.get(user=request.user)
    address=Address.objects.filter(user=request.user)
    contactNumbers=ContactNumbers.objects.filter(user=request.user)
    return render(request,'accounts/profile.html',{'profile':profile,'contactNumbers':contactNumbers,'address':address})

def dashboard():
    pass
