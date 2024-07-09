from django.core.management import BaseCommand

from app_users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@admin.admin')
        user.set_password='admin'
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
