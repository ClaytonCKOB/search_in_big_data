from django.shortcuts import render, HttpResponse

# Create your views here.

def index(response):
    return render(response, 'main/index.html', {})