from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
def index(request):
    return HttpResponse("<p>Hello Word, Hello, Django</p>")
 
def test(request):
    return HttpResponse("<p>Hello test, Hello, Django</p>")