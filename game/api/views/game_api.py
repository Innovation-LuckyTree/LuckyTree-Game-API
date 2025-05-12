from .base_viewset import BaseViewSet
from game.models import Game
from game.api.serializers import BaseGameSerializer

class GameViewset(BaseViewSet):
    queryset = Game.objects.all()
    serializer_class = BaseGameSerializer

