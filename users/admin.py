from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "last_name",
        "first_name",
        "patronymic",
        "avatar",
        "email",
    )
    list_filter = (
        "last_name",
        "first_name",
    )
    search_fields = (
        "last_name",
        "first_name",
        "patronymic",
    )
