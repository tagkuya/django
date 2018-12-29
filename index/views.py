from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World From IndexView")
    
# Create your views here.