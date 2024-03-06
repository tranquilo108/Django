from django.core.management.base import BaseCommand
from myapp.models import Product


class Command(BaseCommand):
    help = "Delete a product."

    def add_arguments(self, parser):
        parser.add_argument('product_id', type=int, help="Product ID")

    def handle(self, *args, **kwargs):
        product_id = kwargs['product_id']
        product = Product.objects.get(pk=product_id)
        product.delete()

        self.stdout.write(f'Product deleted successfully.')
