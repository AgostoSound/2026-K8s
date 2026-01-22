from django.conf import settings
from django.db import models
from .rate import Rate


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    is_active = models.BooleanField(default=True)

    rate = models.ForeignKey(
        Rate,
        on_delete=models.PROTECT,
        related_name="products",
        null=True,
        default=None
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="products_created",
        null=True,
        default=None
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products_updated",
        default=None
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
