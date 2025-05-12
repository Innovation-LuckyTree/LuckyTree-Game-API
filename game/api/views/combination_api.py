from .base_viewset import BaseViewSet
from game.models import Combination
from game.api.serializers import CombinationSerializer

class CombinationViewset(BaseViewSet):
    queryset = Combination.objects.all()
    serializer_class = CombinationSerializer