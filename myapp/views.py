from django.shortcuts import render
from django.http import HttpResponse


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
