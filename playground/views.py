from django.shortcuts import render
from django.http import HttpResponse
from mysql.connector import connect, Error
from .models import *


# Create your views here.


def hello(request):
    x = Book.objects.all()
    print(x)
    #return render(request,'hello.html',{'name': 'x'})

    

    
