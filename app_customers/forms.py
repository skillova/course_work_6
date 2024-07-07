from django import forms

from app_customers.models import Customers


class CustomersForm(forms.ModelForm):
    """
    model = <model> Указываем модель, импортируем из <app_name>.models.
    fields = () Список полей для отображения. Значение '__all__' - Использование всех полей модели.
    exclude = () Использование всех полей, кроме перечисленных.
    """

    class Meta:
        model = Customers
        fields = (
            'last_name',
            'first_name',
            'patronymic',
            'avatar',
            'email',
            'description',
        )
