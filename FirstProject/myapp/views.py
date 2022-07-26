from django.http import HttpResponse
from django.shortcuts import render
import random

# Create your views here.

num=1

def index(request):
    #return HttpResponse("This is Django Project")
    dt={'data':'Mitesh'}
    return render(request,'index.html',dt)

def about(request):
    #num=random.randint(1111,9999)
    global num
    num+=1
    return render(request,'about.html',{'num':num})

def contact(request):
    return render(request,'contact.html')