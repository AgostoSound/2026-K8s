from django.conf import settings
from django.db import models
from .product import Product


class Reservation(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reservations",
        null=True,
        default=None
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="reservations",
        null=True
    )

    notes = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Reservation #{self.id} - user={self.user_id} product={self.product_id}"
