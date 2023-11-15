from django import forms
from django.core import validators
from .models import User


class Form(forms.ModelForm): 
  class Meta:
   model = User
   fields = ['name','email','password']
   widgets = {
   'name': forms.TextInput(attrs={'class':'form-control'}),
   'email': forms.EmailInput(attrs={'class':'form-control'}),
   'message':forms.TextInput(render_value=True, attrs={'class':'form-control'}),
    }
