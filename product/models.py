from django.utils import timezone
from django.db import models
from taggit.managers import TaggableManager
from django.utils.translation import gettext_lazy as _ #as _ , um es als _ zu benutzen
from django.contrib.auth.models import User # um den default User zu importieren und weiter nutzen
from django.utils.text import slugify


PRODUCT_FLAG ={
    ('Sale','Sales'),
    ('Feature','Feature'),
    ('New','New'),
}

# Create your models here.
class Product(models.Model):
    name =models.CharField(_('Name'),max_length=150)
    img= models.ImageField(_('img'),upload_to='products/',default='default.png')
    flag=models.CharField(_('flag'),max_length=10,choices=PRODUCT_FLAG)
    price =models.FloatField(_('price'))
    sku= models.IntegerField(_('sku'))
    brand = models.ForeignKey('Brand',verbose_name=_('brand'),related_name='product_brand',on_delete=models.CASCADE) #CASCADE delete all the related products ,if the brand is deleted
    tags = TaggableManager()
    subtitle = models.TextField(_('subtitle'),max_length=500)
    description = models.TextField(_('description'),max_length=200)
    slug = models.SlugField(null=True,blank=True) # um ein link mit dem Title übereinzustimmen also derselbe Name
    quantitiy =models.IntegerField(default=1)
    def __str__ (self):
        return self.name
    def save (self, *args, **kwargs):
        self.slug =slugify(self.name)
        super(Product,self).save(*args , **kwargs)
'''
name 
flag
img
price
sku
brand
tags
subtitle
description
'''

class Images(models.Model):
    Product = models.ForeignKey(Product,verbose_name=_('product'),related_name='product_image',on_delete=models.CASCADE)
    img=models.ImageField(_('image'),upload_to='product_images/', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return str(self.Product)
'''
img
product: foreignkey
'''

class Reviews(models.Model):
    Product = models.ForeignKey(Product,verbose_name=_('product'),related_name='product_review',on_delete=models.CASCADE)
    user= models.ForeignKey(User,verbose_name=_('user'),related_name='review_author',on_delete=models.SET_NULL , null=True, blank=True) # um die reviews nicht zu löchen falls den User gelöscht ist
    comment = models.CharField(_('comment'),max_length=200)
    rate = models.IntegerField(_("rate"))
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.Product)
'''
rate
user
date
review
product
'''

class Brand(models.Model):
    name =models.CharField(_('brand'),max_length=30)
    img=models.ImageField(_('image'),upload_to='product_images/', height_field=None, width_field=None, max_length=None)
    slug = models.SlugField(null=True,blank=True)
    def __str__(self):
        return self.name

'''
name
img

'''
