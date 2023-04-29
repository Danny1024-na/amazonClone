from django.urls import path
from .views import *

app_name='accounts'

urlpatterns = [
    path('signup/',signUp,name='signup'),
    path('profile/',profile,name='profile'),
]
