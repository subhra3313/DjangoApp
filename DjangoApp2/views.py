import django
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def index(request):
    return HttpResponse('''<h1>Welcome</h1> <a href = " http://127.0.0.1:8000/shop/">Shop </a>???''')