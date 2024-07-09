from django import forms

from app_mailings.models import Message, MailSettings


class MessageForm(forms.ModelForm):
    """
    model = <model> Указываем модель, импортируем из <app_name>.models.
    fields = () Список полей для отображения. Значение '__all__' - Использование всех полей модели.
    exclude = () Использование всех полей, кроме перечисленных.
    """

    class Meta:
        model = Message
        fields = '__all__'


class MailSettingsForm(forms.ModelForm):
    """
    model = <model> Указываем модель, импортируем из <app_name>.models.
    fields = () Список полей для отображения. Значение '__all__' - Использование всех полей модели.
    exclude = () Использование всех полей, кроме перечисленных.
    """

    class Meta:
        model = MailSettings
        fields = '__all__'
