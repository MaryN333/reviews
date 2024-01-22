from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError
from .forms import UserCreateForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# from django.shortcuts import redirect

# Create your views here.


def signupaccount(request):
    if request.method == 'GET':
        return render(request, 'accounts/signupaccount.html', {'form': UserCreateForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'],
                    password=request.POST['password1']
                )
                user.save()
                login(request, user)
                return redirect('restaurant:index')
            except IntegrityError:
                return render(request, 'accounts/signupaccount.html', {'form': UserCreateForm, 'error': 'Username already taken. Choose new username.'})
        else:
            return render(request, 'accounts/signupaccount.html', {'form': UserCreateForm, 'error': 'Passwords do not match'})

# def signupaccount(request):
#     return render(request, 'accounts/signupaccount.html', {'form': UserCreationForm})


@login_required
def logoutaccount(request):
    logout(request)
    return redirect('restaurant:index')


def loginaccount(request):
    if request.method == 'GET':
        return render(request, 'accounts/loginaccount.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request, 'accounts/loginaccount.html', {'form': AuthenticationForm(), 'error': 'username and password do not match'})
        else:
            login(request, user)
            return redirect('restaurant:index')
