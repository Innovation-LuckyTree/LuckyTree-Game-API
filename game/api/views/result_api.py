from .base_viewset import BaseViewSet
from game.models import Result
from game.api.serializers import BaseResultSerializer

class ResultViewset(BaseViewSet):
    queryset = Result.objects.all()
    serializer_class = BaseResultSerializer