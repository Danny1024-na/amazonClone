from django.urls import path
from .views import *

app_name='accounts'

urlpatterns = [
    path('signup/',signUp,name='signup'),
    path('profile/',profile,name='profile'),
    path('dashboard',dashboard,name='dashboard'),
    path('<str:username>/activate',activate,name='activate'),
]
