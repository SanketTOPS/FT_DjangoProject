from django.shortcuts import redirect, render
from .forms import signupForm
from .models import signup_master

# Create your views here.

def userSignup(request):
    newuser=signupForm(request.POST)
    if newuser.is_valid():
        newuser.save()
        print("User created successfully!")
    else:
        print(newuser.errors)
        
def userSignin(request):
    unm=request.POST["username"]
    pas=request.POST["password"]

    user=signup_master.objects.filter(username=unm,password=pas)
    if user: #true
        print("Login successfully!")
    else:
        print("Error....Login fail, Try again.")


def index(request):
    if request.method=="POST":
        if request.POST.get("login")=="login":
            userSignin(request)
            return redirect("notes")
        elif request.POST.get("signup")=="signup":
            userSignup(request)
            return redirect("notes")
    return render(request,'index.html')

def notes(request):
    return render(request,'notes.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')