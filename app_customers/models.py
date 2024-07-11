from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Customers(models.Model):
    #  Django модель клиентов (eng: customers).
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
        upload_to='app_customers/avatars',
        verbose_name="Аватар",
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Email",
    )
    description = models.TextField(
        verbose_name="Описание",
        **NULLABLE,
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name='Пользователь',
    )

    class Meta:
        #  Настройка для наименования одного и набора объектов
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        #  Строковое отображение объекта
        return f"{self.last_name} {self.first_name} {self.patronymic}"
