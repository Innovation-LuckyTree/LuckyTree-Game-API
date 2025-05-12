from .base_viewset import BaseViewSet
from game.models import DrawSchedule
from game.api.serializers import BaseDrawScheduleSerializer
from rest_framework.decorators import action

class DrawScheduleViewset(BaseViewSet):
    queryset = DrawSchedule.objects.all()
    serializer_class = BaseDrawScheduleSerializer