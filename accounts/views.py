from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .models import Account
from .decorators import allowed_user


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_admin = authenticate(
            request, username=username, password=password)

        if user_admin is not None:
            login(request, user_admin)
            return redirect('/')
        else:
            messages.info(request, 'Username or password is incorrect')
            return render(request, 'accounts/login.html', {})

    return render(request, 'accounts/login.html', {})


def logoutUser(request):
    logout(request)
    return redirect('accounts:login')

@login_required(login_url='accounts:login')
@allowed_user(allowed_roles=['user'])
def profileUser(request, username):
    user = User.objects.get(username=username)
    avatar = Account.objects.get(user_id=user.id).avatar

    if str(request.user) != username:
        return redirect('accounts:profile', username=request.user)
    return render(
        request,
        'accounts/profile.html',
        {
            'user': user,
            'avatar': avatar
        })
