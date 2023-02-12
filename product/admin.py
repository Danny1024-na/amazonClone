from django.contrib import admin

# Register your models here.
from .models import Product, Brand, Reviews,Images

class ProductImagesAdmin(admin.TabularInline):
    model = Images


class ProductAdmin(admin.ModelAdmin):
    list_display =['id','name','brand','price']
    list_filter = ['brand','price']
    inlines = [ProductImagesAdmin]
    search_fields = ['name','price']
    list_editable=['name','price','brand']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user','Product','rate','comment','created_at']
    list_filter = ['created_at','rate']


# class BrandAdmin(admin.ModelAdmin):
#     list_display = ['name']
#     inlines = [ProductImagesAdmin]


admin.site.register(Product,ProductAdmin)
admin.site.register(Brand)
admin.site.register(Reviews,ReviewAdmin)
admin.site.register(Images)
