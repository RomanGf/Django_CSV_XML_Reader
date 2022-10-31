from django.urls import path
from .views import loginPage, logoutUser, profileUser

app_name = 'users'

urlpatterns = [
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('profile/<username>/', profileUser, name='profile')
]
