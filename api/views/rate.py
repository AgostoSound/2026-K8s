from rest_framework import viewsets
from api.models import Rate
from api.serializers import RateSerializer


class RateViewSet(viewsets.ModelViewSet):
    serializer_class = RateSerializer
    queryset = Rate.objects.all().order_by("-id")  # <- SIN select_related
