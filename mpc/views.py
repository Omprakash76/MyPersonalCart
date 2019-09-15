from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h2>Hello Welcom Guys at your MY personal Cart</h2>")