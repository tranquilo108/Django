from django.core.management.base import BaseCommand
from myapp.models import Order, Product


class Command(BaseCommand):
    help = "Update order details."

    def add_arguments(self, parser):
        parser.add_argument('order_id', type=int, help="Order ID")
        parser.add_argument('product_ids', nargs='+', type=int, help="Product IDs")

    def handle(self, *args, **kwargs):
        order_id = kwargs['order_id']
        product_ids = kwargs['product_ids']

        order = Order.objects.get(pk=order_id)
        products = Product.objects.filter(id__in=product_ids)

        order.products.set(products)
        order.total_amount = sum(product.price for product in products)
        order.save()

        self.stdout.write(f'Order {order.id} updated successfully.')
