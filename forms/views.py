from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'forms/home.html')


def about(request):
    return render(request, 'forms/about.html')
