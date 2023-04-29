from django.shortcuts import render ,redirect
from .models import Profile,Address,ContactNumbers
from .forms import *
from django.core.mail import send_mail
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
                    f"Welcome {username} \n use this code {{profile.code}} to actiavte ur account... \n Green-Sotre",
                    "danina964@gmail.com",
                    [email],
                    fail_silently=False,
                    )
            return redirect(f'/account/{username}/activate')
    else:
        form = SignUpForm()
        
    return render(request,'accounts/signUp.html',{'form':form})

def activate(request,username):
    pass 

def profile(request):
    profile=Profile.objects.get(user=request.user)
    address=Address.objects.filter(user=request.user)
    contactNumbers=ContactNumbers.objects.filter(user=request.user)
    return render(request,'accounts/profile.html',{'profile':profile,'contactNumbers':contactNumbers,'address':address})

def dashboard():
    pass
