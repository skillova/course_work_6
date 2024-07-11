from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from mailing.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User