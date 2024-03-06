from django.core.management.base import BaseCommand
from myapp.models import Product


class Command(BaseCommand):
    help = "Read all products."

    def handle(self, *args, **kwargs):
        products = Product.objects.all()
        for product in products:
            self.stdout.write(
                f'Product: {product.name}, Description: {product.description}, Price: {product.price}, Quantity: {product.quantity}')
