from datetime import timedelta
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse

from myapp.forms import ClientForm
from myapp.models import Client, Order


# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')


def about(request):
    html = """<!doctype html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport"
                  content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <title>Document</title>
        </head>
        <body>
        <h1 style="text-align: center">This is a text about us</h1>
        <p style="text-align: center">My first Django project</p>
        <p style="text-align: center">And am i</p>
        </body>
        </html>"""
    return HttpResponse(html)


def orders_by_client_id(request):
    form = ClientForm()
    orders_list = None
    if request.method == "POST":
        form = ClientForm(request.POST)
        start_date = get_start_date(form.data.get('period'))
        if form.is_valid:
            client = Client.objects.filter(name=form.data.get('name')).first()
            if client is not None:
                orders_list = []
                orders = Order.objects.filter(client=client, order_date__gte=start_date).prefetch_related(
                    'products')
                for order in orders:
                    product_info = ', '.join([product.name for product in order.products.all()])
                    orders_list.append({'order_id': order.id,
                                        'client': order.client.name,
                                        'products': product_info,
                                        'total_amount': order.total_amount,
                                        'order_date': order.order_date})
    return render(request, 'myapp/orders_of_client.html', {'form': form, 'orders': orders_list})


def get_start_date(period):
    today = timezone.now().date()
    if period == 'week':
        return today - timedelta(days=7)
    elif period == 'month':
        return today - timedelta(days=30)
    elif period == 'year':
        return today - timedelta(days=365)
    else:
        return today