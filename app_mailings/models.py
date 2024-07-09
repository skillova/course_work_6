from django.db import models

from app_customers.models import Customers

NULLABLE = {'blank': True, 'null': True}

STATUS_CHOICES = [
    ('created', 'Создана'),
    ('active', 'Запущена'),
    ('finished', 'Завершена'),
]

INTERVAL_CHOICES = [
    ('once', 'разовая'),
    ('daily', 'ежедневно'),
    ('weekly', 'раз в неделю'),
    ('monthly', 'раз в месяц'),
]

ACTIVE_CHOICES = [
    (True, 'Активна'),
    (False, 'Неактивна'),
]


class Message(models.Model):
    #  Django модель письма (eng: Message).
    title = models.CharField(
        max_length=200,
        verbose_name='Тема',
    )
    content = models.TextField(
        verbose_name='Содержание',
    )

    class Meta:
        #  Настройка для наименования одного и набора объектов
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        #  Строковое отображение объекта
        return self.title


class MailSettings(models.Model):
    #  Django модель настройки рассылки (eng: Message).
    message = models.ForeignKey(
        Message,
        on_delete=models.CASCADE,
        verbose_name='Сообщение',
    )
    sending_to = models.ManyToManyField(
        Customers,
        verbose_name='Адресат',
    )
    description = models.CharField(
        max_length=150,
        verbose_name='Описание',
    )
    start_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Начало рассылки',
    )
    end_date = models.DateTimeField(
        verbose_name='Конец рассылки',
    )
    interval = models.CharField(
        default='once',
        max_length=10,
        choices=INTERVAL_CHOICES,
        verbose_name='Периодичность',
    )
    status = models.CharField(
        default='created',
        max_length=10,
        choices=STATUS_CHOICES,
        verbose_name='Статус',
    )
    is_active = models.BooleanField(
        default=True,
        choices=ACTIVE_CHOICES,
        verbose_name='Активность',
    )

    class Meta:
        #  Настройка для наименования одного и набора объектов
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

    def __str__(self):
        #  Строковое отображение объекта
        return self.description
