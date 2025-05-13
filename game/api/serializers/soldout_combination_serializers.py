from .base_serializer import BaseModelSerializer
from game.models import SoldoutCombination

class BaseSoldoutSerializer(BaseModelSerializer):
    """
    Base serializer for the SoldoutCombination model.
    """
    class Meta:
        model = SoldoutCombination
        fields = '__all__'  
        