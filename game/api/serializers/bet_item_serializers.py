from rest_framework import serializers
from game.models import BetItem, Combination
from .combination_serializers import SimpleCombinationSerializer

class BaseBetItemSerializer(serializers.ModelSerializer):
    """
    Base serializer for the BetItem model.
    """
    combination = SimpleCombinationSerializer()
    class Meta:
        model = BetItem
        fields = '__all__'
        extra_kwargs = {
            'is_deleted': {'read_only': True},
        }

class SimpleBetItemCreateSerializer(serializers.ModelSerializer):
    combination = serializers.CharField() 
    class Meta:
        model = BetItem
        fields=('combination', 'straightAmount', 'rumbleAmount')
        
    def validate_combination(self, value):
        try:
            return Combination.objects.get(value=value)
        except Combination.DoesNotExist:
            raise serializers.ValidationError(f"Combination '{value}' does not exist.")

    def create(self, validated_data):
        return BetItem.objects.create(**validated_data)