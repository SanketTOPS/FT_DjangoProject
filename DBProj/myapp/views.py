from django.shortcuts import render
from .forms import userForm

# Create your views here.

def index(request):
    if request.method=='POST':
        user=userForm(request.POST)
        if user.is_valid():
            user.save()
            print("Your data has been saved!")
        else:
            print(user.errors)
    return render(request,'index.html')