from rest_framework import serializers
from game.models import Winner

class BaseWinnerSerializer(serializers.ModelSerializer):
    """
    Base serializer for the Winner model.
    """
    class Meta:
        model = Winner
        fields = '__all__'
        extra_kwargs = {
            'is_deleted': {'read_only': True},
        }

class SimpleWinnerSerializer(serializers.ModelSerializer):
    
    user_id = serializers.IntegerField(source='bet_item.bet_transaction.user_id')
    class Meta:
        model = Winner
        fields = ('id', 'win_amount', 'rumble_amount', 'bet_item', 'user_id')