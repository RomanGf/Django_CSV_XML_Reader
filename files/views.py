from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import FileModelForm

from .models import File
from .helper.file_parsers import csv_parser, xml_parser
from .helper.check_users import check_users
from users.models import User as MyUser


@login_required(login_url='users:login')
def upload_file_view(request):
    form = FileModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        obj = File.objects.get(activated=False)
        
        list_csv_users = csv_parser(obj.file_name_csv.path)

        list_xml_users = xml_parser(obj.file_name_xml.path)
        
        obj.activated = True
        obj.save()

        list_users = check_users(list_csv_users, list_xml_users)

        for user in list_users:
            MyUser.objects.create(
                username=user['username'],
                password=user['password'],
                date_joined=user['date_joined'],
                avatar=user['avatar'],
            )

    accounts = [{
        'username': x.username,
        'date_joined': x.date_joined,
        'avatar': x.avatar
    } for x in MyUser.objects.all()]

    return render(request, 'users/upload.html', {'form': form,
                                                 'users': accounts})
