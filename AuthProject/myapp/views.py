from django.shortcuts import redirect, render
from .forms import signupForm

# Create your views here.

def index(request):
    return render(request,'index.html')

def usersignup(request):
    if request.method=='POST':
        newuser=signupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("User created successfully!")
            return redirect('home')
        else:
            print(newuser.errors)
    return render(request,'usersignup.html')

def home(request):
    return render(request,'home.html')