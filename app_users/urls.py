from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from app_users.apps import AppUsersConfig
from app_users.views import UserCreateView, email_verification

app_name = AppUsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='app_users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
]
