from django.db import models
from django.contrib.auth.models import User
from utils.generate_code import generate_code

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    user= models.OneToOneField(User, related_name='profile',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile/',default='default.png')
    code = models.CharField(max_length=8 , default=generate_code)

@receiver(post_save,sender=User) #alle Änderungen auf User werden automatisch gespeichert
def create_profile(sender,instance,created,**kwargs): 
    #ob der User hat schon ein Profile oder nicht
    if created:
        Profile.objects.create(
            user=instance
        )



Number_Choices =(
    ('Primary','Primary'),
    ('Secondary','Secondary')
)

class ContactNumbers(models.Model):
    user =models.ForeignKey(User, related_name='user_contacts', on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=Number_Choices)
    number = models.CharField(max_length=20)


Address_Choices =(
    ('Home','Home'),
    ('Office','Office'),
    ('Business','Business'),
    ('Academy','Academy'),
    ('Other','Other'),
)

class Address(models.Model):
    user =models.ForeignKey(User, related_name='user_address', on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=Address_Choices)
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    house =models.CharField(max_length=20)
    notes = models.CharField(max_length=200)