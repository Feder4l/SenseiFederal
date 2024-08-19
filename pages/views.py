from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')

def hakkimizda(request):
    return render(request, 'pages/hakkimizda.html')

def iletisim(request):
   return render(request, 'pages/iletisim.html')