from rest_framework.routers import DefaultRouter
from api.views.product import ProductViewSet
from api.views.reservation import ReservationViewSet
from api.views.rate import RateViewSet

router = DefaultRouter()
router.register("products", ProductViewSet)
router.register("reservations", ReservationViewSet)
router.register("rates", RateViewSet)

urlpatterns = router.urls
