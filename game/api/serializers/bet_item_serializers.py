from .base_serializer import BaseModelSerializer
from game.models import BetItem

class BaseBetItemSerializer(BaseModelSerializer):
    """
    Base serializer for the BetItem model.
    """
    class Meta:
        model = BetItem
        fields = '__all__'