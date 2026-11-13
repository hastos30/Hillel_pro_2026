from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.db import transaction
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserCreationForm


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("catalog:book_list")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("catalog:book_list")

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        with transaction.atomic():
            response = super().form_valid(form)

            customers_group, _ = Group.objects.get_or_create(name="Customers")

            self.object.groups.add(customers_group)

        login(
            self.request,
            self.object,
            backend="django.contrib.auth.backends.ModelBackend",
        )

        return response
