from rest_framework import serializers
from game.models import BetItem

class BaseBetItemSerializer(serializers.ModelSerializer):
    """
    Base serializer for the BetItem model.
    """
    class Meta:
        model = BetItem
        fields = '__all__'