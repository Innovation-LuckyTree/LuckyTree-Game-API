from .base_viewset import BaseViewSet
from game.models import SoldoutCombination
from game.api.serializers import BaseSoldoutSerializer

class SoldoutCombinationViewset(BaseViewSet):
    queryset = SoldoutCombination.objects.all()
    serializer_class = BaseSoldoutSerializer

