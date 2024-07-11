from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}

ACTIVE_CHOICES = [
    (True, 'Активен'),
    (False, 'Неактивен'),
]


class User(AbstractUser):
    username = None

    last_name = models.CharField(
        max_length=50,
        verbose_name="Фамилия",
    )
    first_name = models.CharField(
        max_length=50,
        verbose_name="Имя",
    )
    patronymic = models.CharField(
        max_length=50,
        verbose_name="Отчество",
    )
    avatar = models.ImageField(
        upload_to='app_users/avatars',
        verbose_name="Аватар",
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Email",
    )
    is_active = models.BooleanField(
        default=False,
        help_text="Статус активации"
    )
    token = models.CharField(
        max_length=100,
        verbose_name='Токен',
        **NULLABLE,
    )

    # переопределение полей
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        #  Настройка для наименования одного и набора объектов
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        #  Строковое отображение объекта
        return f"{self.last_name} {self.first_name} {self.patronymic} {self.email}"
