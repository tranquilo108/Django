from django.core.management.base import BaseCommand
from myapp.models import Order


class Command(BaseCommand):
    help = "Delete an order."

    def add_arguments(self, parser):
        parser.add_argument('order_id', type=int, help="Order ID")

    def handle(self, *args, **kwargs):
        order_id = kwargs['order_id']
        order = Order.objects.get(pk=order_id)
        order.delete()

        self.stdout.write(f'Order deleted successfully.')
