from dataclasses import fields
from pyexpat import model
from django import forms
from .models import userInfo,signup_master

class userForm(forms.ModelForm):
    class Meta:
        model=userInfo
        #fields=('firstname','lastname')
        fields='__all__'
    
class signupForm(forms.ModelForm):
    pass