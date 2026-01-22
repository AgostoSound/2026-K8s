from rest_framework import viewsets
from api.models import Reservation
from api.serializers import ReservationSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.select_related("user", "product").order_by("-id")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
