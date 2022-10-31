from django.http import HttpResponse
from django.shortcuts import redirect


def allowed_user(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = list(request.user.groups.values_list(
                    'name', flat=True))[0]

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return decorator


def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = list(request.user.groups.values_list('name', flat=True))[0]

        if group == 'user':
            return redirect('accounts:profile', username=request.user)

        if group == 'admin':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('accounts:login')

    return wrapper_func
