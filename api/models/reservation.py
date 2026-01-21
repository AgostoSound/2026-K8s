from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reservations")
    product = models.ForeignKey("Product", on_delete=models.PROTECT, related_name="reservations")

    start_date = models.DateField()
    end_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user} - {self.product}"
