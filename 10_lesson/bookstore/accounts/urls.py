from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, reverse_lazy

from .views import RegisterView

app_name = "accounts"

urlpatterns = [
    path(
        "register/",
        RegisterView.as_view(),
        name="register",
    ),
    path(
        "login/",
        LoginView.as_view(
            template_name="accounts/login.html",
            redirect_authenticated_user=True,
            next_page=reverse_lazy("catalog:book_list"),
        ),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(
            next_page=reverse_lazy("catalog:book_list"),
        ),
        name="logout",
    ),
]
