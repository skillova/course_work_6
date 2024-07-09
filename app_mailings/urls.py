from django.urls import path

from app_mailings.apps import AppMailingsConfig
from app_mailings.views import MessageCreateView, MessageListView, MessageDetailView, MessageUpdateView, \
    MessageDeleteView

app_name = AppMailingsConfig.name

urlpatterns = [
    path('create', MessageCreateView.as_view(), name='create'),
    path('', MessageListView.as_view(), name='list'),
    path('view/<int:pk>', MessageDetailView.as_view(), name='view'),
    path('update/<int:pk>', MessageUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', MessageDeleteView.as_view(), name='delete'),
]
