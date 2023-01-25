from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

def logins(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])  # 사용자 인증
        login(request, user)  # 로그인
        return render(request, './about/about.html')
    else:
        return render(request, './login/login.html')

def sign(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['userid'], password=request.POST['password1'])
            user.save()
            return redirect('index')
    return render(request, './login/sign.html')