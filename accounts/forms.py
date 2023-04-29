from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class signUpForm(UserCreationForm):
    class Meta:
        model =User
        Fields =[
            'username',
            'email',
            'password1'
            'password2',
        ]

class activate(forms.Form):
    code =forms.CharField(max_length=8)