from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm



def registerPage(request):

    if request.user.is_authenticated:
        return redirect('index')

    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()

                username = form.cleaned_data.get('username')
                messages.success(request, 'Account successfully created for ' + username)

                return redirect('login')

        return render(request, "accounts/register.html", {"form": form})


def loginPage(request):

    if request.user.is_authenticated:
        return redirect('index')

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username or password is incorrect')
                return render(request, "accounts/login.html")

        return render(request, "accounts/login.html")


def logoutUser(request):
    logout(request)
    return redirect('login')