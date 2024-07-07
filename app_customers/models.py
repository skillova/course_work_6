from django.db import models

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

    class Meta:
        #  Настройка для наименования одного и набора объектов
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        #  Строковое отображение объекта
        return f"{self.last_name} {self.first_name} {self.patronymic}"
