from rest_framework import serializers
from game.models import SoldoutCombination

class BaseSoldoutSerializer(serializers.ModelSerializer):
    """
    Base serializer for the SoldoutCombination model.
    """
    class Meta:
        model = SoldoutCombination
        fields = '__all__'  
        extra_kwargs = {
            'is_deleted': {'read_only': True},
        }
        