from rest_framework import serializers
from game.models import CombinationLimit

class BaseCombinationLimitSerializer(serializers.ModelSerializer):
    """
    Base serializer for the CombinationLimit model.
    """
    class Meta:
        model = CombinationLimit
        fields = '__all__'  
        extra_kwargs = {
            'is_deleted': {'read_only': True},
        }
        