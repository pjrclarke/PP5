from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sku',
        'price',
        'description',
        'price',
        'image'         
    )
    ordering = ('sku')
    
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductImage)




# Register your models here.
