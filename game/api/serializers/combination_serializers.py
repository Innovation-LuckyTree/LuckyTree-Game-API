from .base_serializer import BaseModelSerializer
from game.models import Combination

class CombinationSerializer(BaseModelSerializer):
    """
    Base serializer for the Combination model.
    """
    class Meta:
        model = Combination
        fields = '__all__'  
        