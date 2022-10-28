from email import message
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .models import User


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            user = None

        user_admin = authenticate(
            request, username=username, password=password)

        if user is not None and user.password == password:
            return render(request, 'users/profile.html', {'user': user})
        elif user == None and user_admin is not None:
            login(request, user_admin)
            return redirect('/')
        else:
            message.info(request, 'Username or password is incorrect')
            return render(request, 'users/login.html', {})

    return render(request, 'users/login.html', {})


def logoutUser(request):
    logout(request)
    return redirect('users:login')
