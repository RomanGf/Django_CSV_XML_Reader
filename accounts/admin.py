from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from .models import Account


class AccountInLine(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'Users'


class CustomizedUserAdmin(UserAdmin):
    def add_view(self, *args, **kwargs):
        self.inlines = []
        return super(CustomizedUserAdmin, self).add_view(*args, **kwargs)

    def change_view(self, *args, **kwargs):
        self.inlines = [AccountInLine]
        return super(CustomizedUserAdmin, self).change_view(*args, **kwargs)


admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)
admin.site.register(Account)
