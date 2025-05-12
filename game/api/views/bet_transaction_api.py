from .base_viewset import BaseViewSet
from game.models import BetTransaction
from game.api.serializers import BaseBetTransactionSerializer

class BetTransactionViewset(BaseViewSet):
    queryset = BetTransaction.objects.all()
    serializer_class = BaseBetTransactionSerializer