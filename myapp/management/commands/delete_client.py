from django.core.management.base import BaseCommand
from myapp.models import Client


class Command(BaseCommand):
    help = "Delete a client."

    def add_arguments(self, parser):
        parser.add_argument('client_id', type=int, help="Client ID")

    def handle(self, *args, **kwargs):
        client_id = kwargs['client_id']
        client = Client.objects.get(pk=client_id)
        client.delete()

        self.stdout.write(f'Client deleted successfully.')
