from django.http import HttpResponse
from django.shortcuts import render

def index(request):
        return render(request, 'index.html')


def about(request):
    return render(request, 'templates/about.html')

def blog(request):
    return render(request, 'blog.html')

def class1(request):
    return render(request, 'class.html')