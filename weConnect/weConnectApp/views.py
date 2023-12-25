from django.shortcuts import render, redirect, HttpResponse
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . models import Profile
from django.contrib.auth.models import User
from django.urls import reverse

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


def profile(request, user):
    profile_object = User.objects.get(username=user)
    profile = Profile.objects.get(user=profile_object)
    user = profile.user
    
    user = profile.user

    context = {
        'user': user,
        'profile': profile
    }
    return render(request, 'profile.html', context)

def createProfile(request):
    user = request.user
    profile_exists = Profile.objects.filter(user=user).exists()
    if not profile_exists:
        if request.method == 'POST':
            user = request.user
            name = request.POST['name']
            about = request.POST['about']
            profilepic = request.FILES['profilePic']
            DOB = request.POST['DOB']
            Profile.objects.create(user=user, name=name, about=about, profilePic=profilepic, DOB=DOB)
            return redirect(reverse('profile', kwargs={'user': user}))
        else:
            return render(request, 'createProfile.html')
    else:
        return HttpResponse('UserProfile already exists')