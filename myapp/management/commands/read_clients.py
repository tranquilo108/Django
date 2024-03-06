from django.core.management.base import BaseCommand
from myapp.models import Client


class Command(BaseCommand):
    help = "Read all clients."

    def handle(self, *args, **kwargs):
        clients = Client.objects.all()
        for client in clients:
            self.stdout.write(
                f'Client: {client.name}, Email: {client.email}, Phone: {client.phone_number}, Address: {client.address}')
        