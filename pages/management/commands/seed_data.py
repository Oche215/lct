from django.core.management.base import BaseCommand
from pages.models import Product, ContactUs

class Command(BaseCommand):
    help = 'Populates the database with initial data'

    def handle(self, *args, **kwargs):
        data = [
            {'name': 'Wireless Headphones', 'category': 'Electronics', 'price': '79.99', 'stock': '120', },
            {'name': 'Coffee Mug', 'category': 'Home & Kitchen', 'price': '12.5', 'stock': '300', },

        ]

        for item in data:
            # get_or_create prevents duplicate entries if the script is run multiple times
            obj, created = Product.objects.get_or_create(name=item['name'], defaults={'category': item['category'], 'price': item['price'], 'stock': item['stock'], })

            if created:
                self.stdout.write(self.style.SUCCESS(f"Created {item['name']}"))
            else:
                self.stdout.write(f"{item['name']} already exists.")
