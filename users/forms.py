from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Username '}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter Your Email Address '}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password '}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your Password '}))
    
    class Meta:
        model=User
        fields= ['username', 'email','password1', 'password2']

       