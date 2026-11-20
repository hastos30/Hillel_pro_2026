from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand

from catalog.models import Book


class Command(BaseCommand):
    help = "Create and configure user groups for BookStore"

    def handle(self, *args, **options):
        permissions = {
            "add": Permission.objects.get(
                content_type__app_label=Book._meta.app_label,
                content_type__model=Book._meta.model_name,
                codename="add_book",
            ),
            "change": Permission.objects.get(
                content_type__app_label=Book._meta.app_label,
                content_type__model=Book._meta.model_name,
                codename="change_book",
            ),
            "delete": Permission.objects.get(
                content_type__app_label=Book._meta.app_label,
                content_type__model=Book._meta.model_name,
                codename="delete_book",
            ),
        }

        groups = {
            "Customers": [],
            "Managers": [
                permissions["add"],
                permissions["change"],
            ],
            "Administrators": [
                permissions["add"],
                permissions["change"],
                permissions["delete"],
            ],
        }

        for name, group_permissions in groups.items():
            group, created = Group.objects.get_or_create(name=name)

            group.permissions.set(group_permissions)

            action = "Created" if created else "Updated"

            self.stdout.write(self.style.SUCCESS(f"{action} group: {name}"))

        self.stdout.write(self.style.SUCCESS("All groups configured successfully."))
