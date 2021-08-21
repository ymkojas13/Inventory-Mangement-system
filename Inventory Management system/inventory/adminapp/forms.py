from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
'''class Signform(UserCreationForm):
    password2=forms.CharField(label='confirm password (again)',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email:Email'}'''

class Signform(forms.Form):
    Username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
    }))
    Firstname = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',

    }))
    Lastname = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
    }))
    Email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email address',
    }))
    Contact = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'contact number',
    }))
    Password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'type': 'password'
    }))
    Confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'confirm_Password',
        'type': 'confirm_password'
    }))



class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'type': 'password'
    }))