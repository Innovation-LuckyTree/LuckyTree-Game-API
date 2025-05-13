from .base_serializer import BaseModelSerializer
from game.models import Winner

class BaseWinnerSerializer(BaseModelSerializer):
    """
    Base serializer for the Winner model.
    """
    class Meta:
        model = Winner
        fields = '__all__'