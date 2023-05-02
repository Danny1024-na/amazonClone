from django.db import models
from django.utils import timezone
from product.models import Product
from django.contrib.auth.models import User
from utils.generate_code import generate_code
# Create your models here.

CART_STATUS =(
    ('Inprogress','Inprogress'),
    ('Completed', 'Completed'),
)

class Cart(models.Model):
    user = models.ForeignKey(User,related_name="cart_order",on_delete=models.SET_NULL,null=True,blank=True)
    orderStatus= models.CharField(max_length=12,choices=CART_STATUS,default='Inprogress')

    # def __str__(self):
    #     return self.order_code

    def cart_total(self):
        total=0
        for product in self.cart_detail.all():
            total += round(product.total,2)
        return round(total,2)


class Cartdetail(models.Model):
    cart=models.ForeignKey(Cart,related_name='cart_detail',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='cart_Product',on_delete=models.SET_NULL,null=True,blank=True)
    price=models.FloatField(null=True,blank=True)
    total =models.FloatField(null=True,blank=True)
    quantitiy =models.IntegerField(default=1)

    def __str__(self) -> str:
        return str(self.product)

    def save(self, *args, **kwargs):
       self.total=self.price*self.quantitiy
       super(Cartdetail, self).save(*args, **kwargs) # Call the real save() method


ORDER_STATUS =(
    ('Recieved','Recieved'),
    ('Processed', 'Processed'),
    ('Shipped', 'Shipped'),
    ('Delivered','Delivered'),
)


class Order(models.Model):
    order_code=models.CharField(max_length=10,default=generate_code)
    user = models.ForeignKey(User,related_name="user_order",on_delete=models.SET_NULL,null=True,blank=True)
    orderStatus= models.CharField(max_length=12,choices=ORDER_STATUS,default='Recieved')
    deliveryDate=models.DateTimeField(null=True,blank=True)
    orderDate=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.order_code


class Orderdetail(models.Model):
    order=models.ForeignKey(Order,related_name='order_detail',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='order_Product',on_delete=models.SET_NULL,null=True,blank=True)
    price=models.FloatField()
    total =models.FloatField(null=True,blank=True)
    quantitiy =models.IntegerField(default=1)

    def __str__(self) -> str:
        return str(self.order)

    def save(self, *args, **kwargs):
       self.total=self.price*self.quantitiy
       super(Orderdetail, self).save(*args, **kwargs) # Call the real save() method