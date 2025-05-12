from .base_viewset import BaseViewSet
from game.models import CompanyGame
from game.api.serializers import BaseCompanyGameSerializer

class CompanyGameViewset(BaseViewSet):
    queryset = CompanyGame.objects.all()
    serializer_class = BaseCompanyGameSerializer

