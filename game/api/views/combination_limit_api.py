from .base_viewset import BaseViewSet
from game.models import CombinationLimit
from game.api.serializers import BaseCombinationLimitSerializer

class CombinationLimitViewset(BaseViewSet):
    queryset = CombinationLimit.objects.all()
    serializer_class = BaseCombinationLimitSerializer

