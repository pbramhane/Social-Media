from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mylogin')
    
    context = {'registerform': form}

    return render(request, 'register.html', context)

def myLogin(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
    
    context = {'loginform': form}

    return render(request, 'mylogin.html', context)

@login_required(login_url='mylogin')
def home(request):
    return render(request, 'home.html')


def myLogout(request):
    auth.logout(request)
    return redirect('mylogin')