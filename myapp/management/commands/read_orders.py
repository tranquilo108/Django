from django.core.management.base import BaseCommand
from myapp.models import Order

class Command(BaseCommand):
    help = "Read all orders."

    def handle(self, *args, **kwargs):
        orders = Order.objects.all()
        for order in orders:
            product_info = ', '.join([product.name for product in order.products.all()])
            self.stdout.write(f'Order ID: {order.id}, Client: {order.client.name}, Products: {product_info}, Total Amount: {order.total_amount}, Order Date: {order.order_date}')
