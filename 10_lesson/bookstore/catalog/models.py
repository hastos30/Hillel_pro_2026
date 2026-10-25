from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Назва категорії")

    slug = models.SlugField(
        max_length=120, unique=True, allow_unicode=True, verbose_name="Slug"
    )

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="Назва книги")

    author = models.CharField(max_length=150, verbose_name="Автор")

    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")

    description = models.TextField(blank=True, verbose_name="Опис")

    stock = models.PositiveIntegerField(default=0, verbose_name="Кількість на складі")

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="books",
        verbose_name="Категорія",
    )

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ["title"]

    def __str__(self):
        return self.title
