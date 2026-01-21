from rest_framework.viewsets import ModelViewSet
from api.models import Rate
from api.serializers import RateSerializer

class RateViewSet(ModelViewSet):
    queryset = Rate.objects.select_related("user", "product").all()
    serializer_class = RateSerializer
