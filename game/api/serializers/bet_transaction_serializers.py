from rest_framework import serializers
from game.models import BetTransaction

class BaseBetTransactionSerializer(serializers.ModelSerializer):
    """
    Base serializer for the BetTransaction model.
    """
    class Meta:
        model = BetTransaction
        fields = '__all__'
        extra_kwargs = {
            'is_deleted': {'read_only': True},
        }