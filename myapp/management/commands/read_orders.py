from django.core.management.base import BaseCommand
from myapp.models import Order


class Command(BaseCommand):
    help = "Read all orders."

    def handle(self, *args, **kwargs):
        orders = Order.objects.all()
        for order in orders:
            product_info = ', '.join([product.name for product in order.products.all()])
            self.stdout.write(f'Order ID: {order.id}, '
                              f'Client: {order.client.name}, '
                              f'Products: {product_info}, '
                              f'Total Amount: {order.total_amount}, '
                              f'Order Date: {order.order_date}')
