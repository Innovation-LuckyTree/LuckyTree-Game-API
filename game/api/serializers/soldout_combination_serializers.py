from rest_framework import serializers
from game.models import SoldoutCombination

class BaseSoldoutSerializer(serializers.ModelSerializer):
    """
    Base serializer for the SoldoutCombination model.
    """
    class Meta:
        model = SoldoutCombination
        fields = '__all__'  
        