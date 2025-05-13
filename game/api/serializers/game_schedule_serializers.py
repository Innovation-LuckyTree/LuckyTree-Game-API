from .base_serializer import BaseModelSerializer
from game.models import GameSchedule

class BaseGameScheduleSerializer(BaseModelSerializer):
    """
    Serializer for the GameSchedule model.
    """
    class Meta:
        model = GameSchedule
        fields = '__all__'  