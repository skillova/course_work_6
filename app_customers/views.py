from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from app_customers.forms import CustomersForm
from app_customers.models import Customers


class CustomerCreateView(LoginRequiredMixin, CreateView): #миксин добавить
    """
    CreateView — отвечает за создание объекта, для него название шаблона: <app_name>/<model>_form.html
    """

    model = Customers  # Модель
    form_class = CustomersForm  # fields = ('__all__')  # Поля для заполнения при создании
    success_url = reverse_lazy('customers:list')  # Адрес для перенаправления после успешного создания

    def form_valid(self, form): # добавить условие
        customer = form.save()
        user = self.request.user
        customer.owner = user
        customer.save()
        return super().form_valid(form)


class CustomerListView(ListView):
    """
    ListView — отвечает за отображение списка объектов, для него название шаблона: <app_name>/<model>_list.html
    """

    model = Customers  # Модель

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        self.object = form.save()
        user = self.request.user
        self.object.owner = user
        self.object.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        else:
            return self.form_invalid(form)
        return super().form_valid(form)


class CustomerDetailView(DetailView):
    """
    DetailView — отвечает за просмотр деталей объекта, название шаблона: <app_name>/<model>_detail.html
    """

    model = Customers  # Модель


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    """
    UpdateView — отвечает за редактирование объекта, для него название шаблона: <app_name>/<model>_form.html
    """

    model = Customers  # Модель
    form_class = CustomersForm  # fields = ('__all__')  # Поля для заполнения при создании
    success_url = reverse_lazy('customers:list')  # Адрес для перенаправления после успешного создания

    def form_valid(self, form):
        customer = form.save()
        user = self.request.user
        customer.owner = user
        customer.save()
        return super().form_valid(form)


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    """
    DeleteView — отвечает за удаление объекта, для него название шаблона: <app_name>/<model>_confirm_delete.html
    """

    model = Customers  # Модель
    success_url = reverse_lazy('customers:list')  # Адрес для перенаправления после успешного создания
