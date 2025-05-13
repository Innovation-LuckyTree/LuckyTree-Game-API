from .base_serializer import BaseModelSerializer
from game.models import Result

class BaseResultSerializer(BaseModelSerializer):
    """
    Base serializer for the Result model.
    """
    class Meta:
        model = Result
        fields = '__all__'