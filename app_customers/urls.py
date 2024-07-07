from django.urls import path

from app_customers.apps import AppCustomersConfig
from app_customers.views import CustomerCreateView, CustomerListView, CustomerDetailView, CustomerUpdateView, \
    CustomerDeleteView

app_name = AppCustomersConfig.name

urlpatterns = [
    path('create', CustomerCreateView.as_view(), name='create'),
    path('', CustomerListView.as_view(), name='list'),
    path('view/<int:pk>', CustomerDetailView.as_view(), name='view'),
    path('update/<int:pk>', CustomerUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', CustomerDeleteView.as_view(), name='delete'),
]
