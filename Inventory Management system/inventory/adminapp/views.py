from django.shortcuts import render,HttpResponseRedirect, redirect
from .forms import Signform,LoginForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

def sign_up(request):
    if request.method=="POST":
        fm=Signform(request.POST)
        if fm.is_valid():
            Username = fm.cleaned_data['Username']
            Firstname = fm.cleaned_data['Firstname']
            Lastname = fm.cleaned_data['Lastname']
            Email = fm.cleaned_data['Email']
            Contact= fm.cleaned_data['Contact']
            Password = fm.cleaned_data['Password']
            Confirm_password = fm.cleaned_data['Confirm_password']
            onlinestore = authenticate(Username=Username,Firstname=Firstname, Lastname=Lastname, Email=Email, Contact=Contact,Password=Password, Confirm_password=Confirm_password)
            onlinestore.save()
            messages.success(request,'you have signup successfully')
            fm.save()
    else:
        fm=Signform()
    return render(request,'signup.html',{'form':fm})

def user_login(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'you have signup successfully')
                return redirect('dashboard')
    context = {'form': forms}
    return render(request, 'login.html', context)


def user_profile(request):
    if request.user.is_authenticated:
        return render(request,'dashboard.html',{'name':request.user})
    else:
        return HttpResponseRedirect('/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')



def set_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Password set successfully')
                #return HttpResponseRedirect('/profile')
        else:
            fm = SetPasswordForm(user=request.user)
        return render(request,'setpassword.html',{'form':fm})
    else:
        return HttpResponseRedirect('/')
