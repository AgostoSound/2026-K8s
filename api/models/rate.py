from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class Rate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rates")
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="rates")

    score = models.PositiveSmallIntegerField()  # 1–5
    comment = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "product")

    def __str__(self) -> str:
        return f"{self.product} - {self.score}"
