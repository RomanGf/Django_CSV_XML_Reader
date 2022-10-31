from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    avatar = models.CharField(max_length=255, default="https://pbs.twimg.com/media/BcINeMVCIAABeWd.jpg")
    
    def __str__(self):
        return f'Username: {self.avatar}'