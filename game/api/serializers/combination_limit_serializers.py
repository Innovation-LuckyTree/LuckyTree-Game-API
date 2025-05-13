from .base_serializer import BaseModelSerializer
from game.models import CombinationLimit

class BaseCombinationLimitSerializer(BaseModelSerializer):
    """
    Base serializer for the CombinationLimit model.
    """
    class Meta:
        model = CombinationLimit
        fields = '__all__'  
        