from django.shortcuts import redirect, render
from .forms import signupForm, notesForm
from .models import signup_master
from django.contrib.auth import logout

# Create your views here.
"""
def userSignup(request):
    newuser=signupForm(request.POST)
    if newuser.is_valid():
        newuser.save()
        print("User created successfully!")
    else:
        print(newuser.errors)"""
        
"""def userSignin(request):
    unm=request.POST["username"]
    pas=request.POST["password"]

    user=signup_master.objects.filter(username=unm,password=pas)
    if user: #true
        print("Login successfully!")
    else:
        print("Error....Login fail, Try again.")"""


def index(request):
    if request.method=="POST":
        if request.POST.get("login")=="login":
            unm=request.POST["username"]
            pas=request.POST["password"]
            user=signup_master.objects.filter(username=unm,password=pas)

            userid=signup_master.objects.get(username=unm)
            print("UserID:",userid.id)
            if user:
                print("Login Successfull!")
                request.session["user"]=unm
                request.session["userid"]=userid.id
                return redirect("notes")
            else:
                print("Error...Login fail! Try again.")
        elif request.POST.get("signup")=="signup":
            newuser=signupForm(request.POST)
            if newuser.is_valid():
                newuser.save()
                print("User created successfully!")
                return redirect("notes")
            else:
                print(newuser.errors)
    return render(request,'index.html')


def notes(request):
    user=request.session.get("user")
    if request.method=="POST":
        mynote=notesForm(request.POST, request.FILES)
        if mynote.is_valid():
            mynote.save()
            print("Your post has been uploaded!")
        else:
            print(mynote.errors)
    return render(request,'notes.html',{'user':user})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def userlogout(request):
    logout(request)
    return redirect("/")

def updateprofile(request):
    user=request.session.get("user")
    userid=request.session.get("userid")
    uid=signup_master.objects.get(id=userid)
    return render(request,'updateprofile.html',{'user':user,"cuser":signup_master.objects.get(id=userid)})