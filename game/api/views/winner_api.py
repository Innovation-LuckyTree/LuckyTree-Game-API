from .base_viewset import BaseViewSet
from game.models import Winner
from game.api.serializers import BaseWinnerSerializer

class WinnerViewset(BaseViewSet):
    queryset = Winner.objects.all()
    serializer_class = BaseWinnerSerializer