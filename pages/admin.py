from django.contrib import admin
from .models import ContactUs, Product

# Register your models here.
admin.site.register(ContactUs)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'created_at')
    search_fields = ('name', 'category')
    list_filter = ('category',)
