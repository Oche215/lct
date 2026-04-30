from django.contrib import admin
from .models import ContactUs, Product, Sales, Inventory

# Register your models here.
admin.site.register(ContactUs)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'created_at')
    search_fields = ('name', 'category')
    list_filter = ('category',)

@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = ('order_date', 'region', 'manager', 'salesman', 'product', 'unit', 'price', 'amount')

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'name', 'initial_stock', 'stock_in', 'stock_sold', 'available_stock', 'unit_price', 'total_amount')