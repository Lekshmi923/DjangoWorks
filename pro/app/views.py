from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def Home(request):

    print(request.method)
    if(request.method=="GET"):
        return HttpResponse("Welcome to Django")

def Index(request):
    if(request.method=="GET"):
        return HttpResponse("Index")