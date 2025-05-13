from .base_serializer import BaseModelSerializer
from game.models import DrawSchedule

class BaseDrawScheduleSerializer(BaseModelSerializer):
    """
    Serializer for the DrawSchedule model.
    """
    class Meta:
        model = DrawSchedule
        fields = '__all__'  