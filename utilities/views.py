from django.contrib.auth import login
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm


# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('products:products-home')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('utilities:login_user')
    else:
        return render(request, 'login.html')


def logout_user(request):
    auth.logout(request)
    return redirect('products:products-home')


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already registered')
                return redirect('utilities:sign-up')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already Registered Before')
                return redirect('utilities:sign-up')
            else:
                user = User.objects.create_user(username=username, password=password,
                                                email=email, first_name=first_name, last_name=last_name)
                user.save()

                return redirect('utilities:login_user')


        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect('utilities:sign-up')

    else:
        return render(request, 'signup.html')
