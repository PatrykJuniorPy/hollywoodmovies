from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def hello(request):
    s = request.GET.get('s', '')
    return HttpResponse(f'<strong>Hello, {s} world!</strong>')