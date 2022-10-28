from distutils.command.upload import upload
from django.db import models

# Create your models here.
from email.policy import default
import datetime
from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=255, default='admin')
    date_joined = models.DateField(default=datetime.date.fromtimestamp(1421161336))
    avatar = models.CharField(max_length=255, default="https://pbs.twimg.com/media/BcINeMVCIAABeWd.jpg")
    
    def __str__(self):
        return f'Username: {self.username}'