from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.db.models import Q

from .forms import FileModelForm
from .models import File

from .helper.file_parsers import parse_csv_file, parse_xml_file
from .helper.check_users import check_users

from accounts.models import Account
from accounts.decorators import admin_only


@login_required(login_url='accounts:login')
@admin_only
def upload_file_view(request):
    form = FileModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        obj = File.objects.get(activated=False)

        list_csv_users = parse_csv_file(obj.file_name_csv.path)

        list_xml_users = parse_xml_file(obj.file_name_xml.path)

        obj.activated = True
        obj.save()

        list_users = check_users(list_csv_users, list_xml_users)

        for user in list_users:
            User.objects.create_user(
                username=user['username'],
                password=user['password'],
                date_joined=user['date_joined'],
            )
            current_user = User.objects.latest('id')
            group = Group.objects.get(name='user')
            group.user_set.add(current_user)

            Account.objects.create(
                avatar=user['avatar'],
                user_id=current_user.id
            )

    accounts = [{
        'id': x.id,
        'username': x.username,
        'date_joined': x.date_joined,
        'avatar': Account.objects.get(user_id=x.id).avatar
    } for x in User.objects.filter(~Q(id=1))]

    return render(
        request,
        'accounts/upload.html',
        {
            'form': form,
            'users': accounts,
        })
