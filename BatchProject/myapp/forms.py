from dataclasses import fields
from pyexpat import model
from django import forms
from .models import signup_master, mynotes


class signupForm(forms.ModelForm):
    class Meta:
        model=signup_master
        fields='__all__'

class notesForm(forms.ModelForm):
    class Meta:
        model=mynotes
        fields='__all__'