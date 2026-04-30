from wsgiref.handlers import format_date_time

from django.db import models

# Define choices as a tuple of tuples (value, human-readable label)
CHOICES = [
    ('default', '------------------ Select a subject  ---------------------------------'),
    ('inquiry', 'Inquiry'),
    ('support', 'Support Request'),
    ('freelance', 'Freelance Job Opportunities'),
    ('connect', 'Request to connect/meet'),
]

# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=220, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=20, blank=False, )
    email = models.EmailField(
        max_length=254,  # Optional, default is 254
        blank=False,  # Field must be filled in forms
        null=False,  # Field cannot be NULL in the database
        help_text="Enter a valid email address"
    )
    message = models.TextField(max_length=360, blank=False)
    subject = models.CharField(
        max_length=50,
        choices=CHOICES,  # This makes it a dropdown in forms/admin
        default='default',  # Optional default value
    )

    class Meta:
        verbose_name_plural = 'Contact Us'

    def __str__(self):
        return f"{self.name} ({self.email})"

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)  # Auto-increment ID
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp

    def __str__(self):
        return f"{self.name} ({self.category})"


class Sales(models.Model):
    order_date = models.DateTimeField()
    region = models.CharField(max_length=200)
    manager = models.CharField(max_length=100)
    salesman = models.CharField(max_length=100)
    product = models.CharField(max_length=220, blank=False)
    unit = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.salesman} ({self.region})"


class Inventory(models.Model):
    product_id = models.AutoField(primary_key=True)  # Auto-increment ID
    name = models.CharField(max_length=100)
    initial_stock = models.PositiveIntegerField()
    stock_in = models.PositiveIntegerField()
    stock_sold = models.PositiveIntegerField()
    available_stock = models.PositiveIntegerField()

    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.name} (Stock In Hand: {self.available_stock})"