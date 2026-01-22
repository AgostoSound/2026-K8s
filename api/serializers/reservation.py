from rest_framework import serializers
from api.models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ["id", "user", "product", "notes", "created_at"]
        read_only_fields = ["id", "created_at", "user"]
