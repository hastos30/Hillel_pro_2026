from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Book, Category


class BookListView(ListView):
    model = Book
    template_name = "catalog/book_list.html"
    context_object_name = "books"
    paginate_by = 6

    def get_queryset(self):
        queryset = Book.objects.select_related("category")

        search = self.request.GET.get("search", "").strip()
        category = self.request.GET.get("category", "").strip()
        availability = self.request.GET.get("availability", "")

        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | Q(author__icontains=search)
            )

        if category:
            queryset = queryset.filter(category__slug=category)

        if availability == "in_stock":
            queryset = queryset.filter(stock__gt=0)

        return queryset.order_by("title")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["categories"] = Category.objects.all()
        context["search"] = self.request.GET.get("search", "")
        context["selected_category"] = self.request.GET.get("category", "")
        context["selected_availability"] = self.request.GET.get("availability", "")

        return context


class BookDetailView(DetailView):
    model = Book
    template_name = "catalog/book_detail.html"
    context_object_name = "book"

    def get_queryset(self):
        return Book.objects.select_related("category")


class BookCreateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    CreateView,
):
    model = Book
    template_name = "catalog/book_form.html"
    fields = [
        "title",
        "author",
        "price",
        "description",
        "stock",
        "category",
    ]

    permission_required = "catalog.add_book"
    success_url = reverse_lazy("catalog:book_list")


class BookUpdateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UpdateView,
):
    model = Book
    template_name = "catalog/book_form.html"
    fields = [
        "title",
        "author",
        "price",
        "description",
        "stock",
        "category",
    ]

    permission_required = "catalog.change_book"
    success_url = reverse_lazy("catalog:book_list")


class BookDeleteView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DeleteView,
):
    model = Book
    template_name = "catalog/book_confirm_delete.html"

    permission_required = "catalog.delete_book"
    success_url = reverse_lazy("catalog:book_list")
