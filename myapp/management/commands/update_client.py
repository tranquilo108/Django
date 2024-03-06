from django.core.management.base import BaseCommand
from myapp.models import Client


class Command(BaseCommand):
    help = "Update client details."

    def add_arguments(self, parser):
        parser.add_argument('client_id', type=int, help="Client ID")
        parser.add_argument('name', type=str, help="Client name")
        parser.add_argument('email', type=str, help="Client email")
        parser.add_argument('phone_number', type=str, help="Client phone number")
        parser.add_argument('address', type=str, help="Client address")

    def handle(self, *args, **kwargs):
        client_id = kwargs['client_id']
        name = kwargs['name']
        email = kwargs['email']
        phone_number = kwargs['phone_number']
        address = kwargs['address']

        client = Client.objects.get(pk=client_id)
        client.name = name
        client.email = email
        client.phone_number = phone_number
        client.address = address
        client.save()

        self.stdout.write(f'Client {client.name} updated successfully.')
