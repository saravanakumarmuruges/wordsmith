from django.shortcuts import render
from django.http import HttpResponse
from .models import blogs

def blog(request):
    data = blogs.objects.all()
    return HttpResponse(data)