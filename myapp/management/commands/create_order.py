from django.core.management.base import BaseCommand
from myapp.models import Order, Client, Product


class Command(BaseCommand):
    help = "Create a new order."

    def add_arguments(self, parser):
        parser.add_argument('client_id', type=int, help="Client ID")
        parser.add_argument('product_ids', nargs='+', type=int, help="Product IDs")

    def handle(self, *args, **kwargs):
        client_id = kwargs['client_id']
        product_ids = kwargs['product_ids']

        client = Client.objects.get(pk=client_id)
        order = Order.objects.create(client=client, total_amount=0)

        products = Product.objects.filter(id__in=product_ids)
        order.products.set(products)

        order.total_amount = sum(product.price for product in products)
        order.save()

        self.stdout.write(f'Order {order.id} created successfully.')
