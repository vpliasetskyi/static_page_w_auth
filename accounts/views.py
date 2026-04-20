from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home(request):
    return render(request, 'home.html')

@login_required
def contact(request):
    return render(request, 'contact.html')

@login_required
def page1(request):
    return render(request, 'page1.html')

@login_required
def page2(request):
    return render(request, 'page2.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password != password2:
            messages.error(request, 'Passwords do not match.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Account created. Please log in.')
            return redirect('login')
    return render(request, 'register.html')


def logout_view(request):
    logout(request)
    return redirect('home')

# Create your views here.
