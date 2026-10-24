from django.db.models import Q, Count, Avg

from .models import Book, Category


def run_examples():

    cheap_books = Book.objects.filter(price__lt=500)

    available_books = Book.objects.filter(stock__gt=0)

    selected_books = Book.objects.filter(
        Q(author__icontains="Tolkien") | Q(price__lte=400)
    )

    categories_stats = Category.objects.annotate(
        books_count=Count("books"), avg_price=Avg("books__price")
    ).values("name", "books_count", "avg_price")

    print("\nCheap books:")
    print(list(cheap_books.values("title", "price")))

    print("\nAvailable books:")
    print(list(available_books.values("title", "stock")))

    print("\nSelected books:")
    print(list(selected_books.values("title", "price")))

    print("\nCategories statistics:")
    print(list(categories_stats))
