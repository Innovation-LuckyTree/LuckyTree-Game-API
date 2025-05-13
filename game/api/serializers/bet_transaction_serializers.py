from .base_serializer import BaseModelSerializer
from game.models import BetTransaction

class BaseBetTransactionSerializer(BaseModelSerializer):
    """
    Base serializer for the BetTransaction model.
    """
    class Meta:
        model = BetTransaction
        fields = '__all__'