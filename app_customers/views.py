from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from app_customers.forms import CustomersForm
from app_customers.models import Customers


class CustomerCreateView(CreateView):
    """
    CreateView — отвечает за создание объекта, для него название шаблона: <app_name>/<model>_form.html
    """

    model = Customers  # Модель
    form_class = CustomersForm  # fields = ('__all__')  # Поля для заполнения при создании
    success_url = reverse_lazy('customers:list')  # Адрес для перенаправления после успешного создания


class CustomerListView(ListView):
    """
    ListView — отвечает за отображение списка объектов, для него название шаблона: <app_name>/<model>_list.html
    """

    model = Customers  # Модель


class CustomerDetailView(DetailView):
    """
    DetailView — отвечает за просмотр деталей объекта, название шаблона: <app_name>/<model>_detail.html
    """

    model = Customers  # Модель


class CustomerUpdateView(UpdateView):
    """
    UpdateView — отвечает за редактирование объекта, для него название шаблона: <app_name>/<model>_form.html
    """

    model = Customers  # Модель
    form_class = CustomersForm  # fields = ('__all__')  # Поля для заполнения при создании
    success_url = reverse_lazy('customers:list')  # Адрес для перенаправления после успешного создания


class CustomerDeleteView(DeleteView):
    """
    DeleteView — отвечает за удаление объекта, для него название шаблона: <app_name>/<model>_confirm_delete.html
    """

    model = Customers  # Модель
    success_url = reverse_lazy('customers:list')  # Адрес для перенаправления после успешного создания
