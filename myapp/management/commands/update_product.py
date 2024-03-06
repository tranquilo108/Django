from django.core.management.base import BaseCommand
from myapp.models import Product

class Command(BaseCommand):
    help = "Update product details."

    def add_arguments(self, parser):
        parser.add_argument('product_id', type=int, help="Product ID")
        parser.add_argument('name', type=str, help="Product name")
        parser.add_argument('description', type=str, help="Product description")
        parser.add_argument('price', type=float, help="Product price")
        parser.add_argument('quantity', type=int, help="Product quantity")

    def handle(self, *args, **kwargs):
        product_id = kwargs['product_id']
        name = kwargs['name']
        description = kwargs['description']
        price = kwargs['price']
        quantity = kwargs['quantity']

        product = Product.objects.get(pk=product_id)
        product.name = name
        product.description = description
        product.price = price
        product.quantity = quantity
        product.save()

        self.stdout.write(f'Product {product.name} updated successfully.')
