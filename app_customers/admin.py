from django.contrib import admin

from app_customers.models import Customers


@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "last_name",
        "first_name",
        "patronymic",
        "avatar",
        "email",
        "description",
    )
    list_filter = (
        "last_name",
        "first_name",
        "patronymic",
    )
    search_fields = (
        "last_name",
        "first_name",
        "patronymic",
        "description",
    )
