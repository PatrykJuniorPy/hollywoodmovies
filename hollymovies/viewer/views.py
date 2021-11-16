from django.shortcuts import render
from django.http import HttpResponse


def hello_view(request, s0):
    s1 = request.GET.get('s1', '')
    return render (
        request,
        template_name="hello.html",
        context={'adjectives': [s0,s1, 'beatiful', 'wonderful']}
    )