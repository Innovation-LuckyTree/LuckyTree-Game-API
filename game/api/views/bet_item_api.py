from .base_viewset import BaseViewSet
from game.models import BetItem
from game.api.serializers import BaseBetItemSerializer

class BetItemViewset(BaseViewSet):
    queryset = BetItem.objects.all()
    serializer_class = BaseBetItemSerializer