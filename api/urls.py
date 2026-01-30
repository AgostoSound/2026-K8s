from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views.product import ProductViewSet
from api.views.reservation import ReservationViewSet
from api.views.rate import RateViewSet
from api.health import HealthView

router = DefaultRouter()
router.register("products", ProductViewSet)
router.register("reservations", ReservationViewSet)
router.register("rates", RateViewSet)

urlpatterns = [
    path("health/", HealthView.as_view(), name="health"),
    path("", include(router.urls)),
]
