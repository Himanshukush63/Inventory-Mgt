from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand', 'price', 'stock')
    list_filter = ('category', 'brand')
    search_fields = ('name', 'brand', 'model_number')
    ordering = ('name',)
