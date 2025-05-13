from rest_framework import serializers
from game.models import BetTransaction, BetItem
from .bet_item_serializers import SimpleBetItemCreateSerializer

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

        
class BetTransactionCreateSerializer(serializers.ModelSerializer):
    bet_items = SimpleBetItemCreateSerializer(many=True)

    class Meta:
        model = BetTransaction
        fields = ('bet_items', 'user_id', 'transactionType', 'game_schedule')

    def create(self, validated_data):
        bet_item_data = validated_data.pop('bet_items')
        transaction = BetTransaction.objects.create(**validated_data)

        bet_items = [
            BetItem(
                **item,
                bet_transaction=transaction
            ) for item in bet_item_data
        ]
        BetItem.objects.bulk_create(bet_items)

        return transaction