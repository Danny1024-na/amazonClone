from django.contrib import admin

# Register your models here.
from .models import Coupon, Order,Orderdetail,Cart,Cartdetail

class OrderAdmin(admin.ModelAdmin):
    list_display= ['orderStatus','orderDate','order_code','deliveryDate']
    list_filter =['orderStatus','orderDate','order_code']

class OrderDetail(admin.ModelAdmin):
    list_display= ['quantitiy','total','price','product','order']
    list_filter =['price','quantitiy']

admin.site.register(Order,OrderAdmin)
admin.site.register(Orderdetail,OrderDetail)

admin.site.register(Cart)
admin.site.register(Cartdetail)

admin.site.register(Coupon)