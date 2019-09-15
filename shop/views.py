from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'shop/index.html')

def about(request):
    return render(request, 'shop/about.html')

def contect(request):
    return render(request, 'shop/contect.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productView(request):
    return render(request, 'shop/productview.html')

def checkout(request):
    return render(request, 'shop/checkout.html')

def cart(request):
    return render(request, 'shop/cart.html')

def myorder(request):
    return render(request, 'shop/myorder.html')

def login(request):
    return render(request, 'shop/login.html')

def support(request):
    return render(request, 'shop/support.html')