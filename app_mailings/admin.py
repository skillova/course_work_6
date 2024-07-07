from django.contrib import admin

from app_mailings.models import Message, MailSettings


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        'content',
    )
    list_filter = (
        "title",
    )
    search_fields = (
        "title",
        'content',
    )


@admin.register(MailSettings)
class MailSettingsAdmin(admin.ModelAdmin):
    list_display = (
        'description',
        'start_date',
        'end_date',
        'interval',
        'status',
        'is_active',
    )
    list_filter = (
        'start_date',
        'end_date',
        'interval',
        'status',
        'is_active',
    )
    search_fields = (
        "message",
    )
