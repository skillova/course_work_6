from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from app_mailings.forms import MailSettingsForm, MessageForm
from app_mailings.models import Message, MailSettings


class MessageCreateView(CreateView):
    """
    CreateView — отвечает за создание объекта, для него название шаблона: <app_name>/<model>_form.html
    """

    model = Message  # Модель
    form_class = MessageForm  # fields = ('__all__')  # Поля для заполнения при создании
    success_url = reverse_lazy('messages:list')  # Адрес для перенаправления после успешного создания

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        mail_settings_formset = inlineformset_factory(Message, MailSettings, form=MailSettingsForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = mail_settings_formset(self.request.POST)
        else:
            context_data['formset'] = mail_settings_formset()
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        mailing_template = form.save()
        self.object = form.save()
        self.object.owner = self.request.user
        mailing_template.owner = self.object.owner
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
            mailing_template.save()
        return super().form_valid(form)


class MessageListView(ListView):
    """
    ListView — отвечает за отображение списка объектов, для него название шаблона: <app_name>/<model>_list.html
    """

    model = Message  # Модель


class MessageDetailView(DetailView):
    """
    DetailView — отвечает за просмотр деталей объекта, название шаблона: <app_name>/<model>_detail.html
    """

    model = Message  # Модель


class MessageUpdateView(UpdateView):
    """
    UpdateView — отвечает за редактирование объекта, для него название шаблона: <app_name>/<model>_form.html
    """

    model = Message  # Модель
    form_class = MessageForm  # fields = ('__all__')  # Поля для заполнения при создании
    success_url = reverse_lazy('messages:list')  # Адрес для перенаправления после успешного создания

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        mail_settings_formset = inlineformset_factory(Message, MailSettings, form=MailSettingsForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = mail_settings_formset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = mail_settings_formset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class MessageDeleteView(DeleteView):
    """
    DeleteView — отвечает за удаление объекта, для него название шаблона: <app_name>/<model>_confirm_delete.html
    """

    model = Message  # Модель
    success_url = reverse_lazy('mailings:list')  # Адрес для перенаправления после успешного создания
