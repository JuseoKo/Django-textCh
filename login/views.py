from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import User

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
            user = User.objects.create_user(id=request.POST['userid'], password=request.POST['password1'],
                                            email=request.POST['email'])
            user.save()
            user = authenticate(username=request.POST['userid'], password=request.POST['password1'])  # 사용자 인증
            login(request, user)
            return redirect('sns:index')
    return render(request, './login/sign.html')