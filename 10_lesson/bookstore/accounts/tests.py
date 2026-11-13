from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.test import TestCase
from django.urls import reverse

from catalog.models import Book, Category

User = get_user_model()


class AuthenticationTests(TestCase):

    def test_registration_page(self):
        response = self.client.get(reverse("accounts:register"))

        self.assertEqual(response.status_code, 200)

    def test_user_registration(self):
        response = self.client.post(
            reverse("accounts:register"),
            {
                "username": "new_customer",
                "email": "customer@example.com",
                "password1": "SecureTestPassword123!",
                "password2": "SecureTestPassword123!",
            },
        )

        self.assertRedirects(
            response,
            reverse("catalog:book_list"),
        )

        user = User.objects.get(username="new_customer")

        self.assertTrue(user.check_password("SecureTestPassword123!"))

        self.assertTrue(user.groups.filter(name="Customers").exists())

        self.assertEqual(
            str(self.client.session["_auth_user_id"]),
            str(user.pk),
        )

    def test_login(self):
        user = User.objects.create_user(
            username="login_user",
            password="SecureTestPassword123!",
        )

        response = self.client.post(
            reverse("accounts:login"),
            {
                "username": "login_user",
                "password": "SecureTestPassword123!",
            },
        )

        self.assertRedirects(
            response,
            reverse("catalog:book_list"),
        )

        self.assertEqual(
            str(self.client.session["_auth_user_id"]),
            str(user.pk),
        )

    def test_logout(self):
        user = User.objects.create_user(
            username="logout_user",
            password="SecureTestPassword123!",
        )

        self.client.force_login(user)

        response = self.client.post(reverse("accounts:logout"))

        self.assertRedirects(
            response,
            reverse("catalog:book_list"),
        )

        self.assertNotIn(
            "_auth_user_id",
            self.client.session,
        )


class BookPermissionTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(
            name="Fantasy",
            slug="fantasy",
        )

        cls.book = Book.objects.create(
            title="The Hobbit",
            author="Tolkien",
            price="390.00",
            description="Fantasy novel",
            stock=12,
            category=cls.category,
        )

        cls.customer_group = Group.objects.create(name="Customers")

        cls.manager_group = Group.objects.create(name="Managers")

        cls.admin_group = Group.objects.create(name="Administrators")

        permissions = {
            codename: Permission.objects.get(
                content_type__app_label="catalog",
                content_type__model="book",
                codename=codename,
            )
            for codename in (
                "add_book",
                "change_book",
                "delete_book",
            )
        }

        cls.manager_group.permissions.add(
            permissions["add_book"],
            permissions["change_book"],
        )

        cls.admin_group.permissions.add(
            permissions["add_book"],
            permissions["change_book"],
            permissions["delete_book"],
        )

        cls.customer = User.objects.create_user(
            username="customer",
            password="SecureTestPassword123!",
        )
        cls.customer.groups.add(cls.customer_group)

        cls.manager = User.objects.create_user(
            username="manager",
            password="SecureTestPassword123!",
        )
        cls.manager.groups.add(cls.manager_group)

        cls.administrator = User.objects.create_user(
            username="administrator",
            password="SecureTestPassword123!",
        )
        cls.administrator.groups.add(cls.admin_group)

    def test_guest_can_view_catalog(self):
        response = self.client.get(reverse("catalog:book_list"))

        self.assertEqual(response.status_code, 200)

    def test_guest_redirected_to_login(self):
        response = self.client.get(reverse("catalog:book_create"))

        self.assertEqual(response.status_code, 302)
        self.assertIn(
            reverse("accounts:login"),
            response["Location"],
        )

    def test_customer_cannot_create_book(self):
        self.client.force_login(self.customer)

        response = self.client.get(reverse("catalog:book_create"))

        self.assertEqual(response.status_code, 403)

    def test_manager_can_create_book(self):
        self.client.force_login(self.manager)

        response = self.client.get(reverse("catalog:book_create"))

        self.assertEqual(response.status_code, 200)

    def test_manager_can_update_book(self):
        self.client.force_login(self.manager)

        response = self.client.get(
            reverse(
                "catalog:book_update",
                args=[self.book.pk],
            )
        )

        self.assertEqual(response.status_code, 200)

    def test_manager_cannot_delete_book(self):
        self.client.force_login(self.manager)

        response = self.client.get(
            reverse(
                "catalog:book_delete",
                args=[self.book.pk],
            )
        )

        self.assertEqual(response.status_code, 403)

    def test_administrator_can_delete_book(self):
        self.client.force_login(self.administrator)

        response = self.client.get(
            reverse(
                "catalog:book_delete",
                args=[self.book.pk],
            )
        )

        self.assertEqual(response.status_code, 200)

    def test_customer_can_view_book_details(self):
        self.client.force_login(self.customer)

        response = self.client.get(
            reverse(
                "catalog:book_detail",
                args=[self.book.pk],
            )
        )

        self.assertEqual(response.status_code, 200)
