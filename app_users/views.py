from django.urls import reverse_lazy
from django.views.generic import CreateView

from app_users.forms import UserRegisterForm
from app_users.models import User


class UserCreateView(CreateView):
    # Создаем обычный контроллер на создание сущности
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
