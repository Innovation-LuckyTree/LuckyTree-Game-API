from rest_framework import serializers
from game.models import Combination

class CombinationSerializer(serializers.ModelSerializer):
    """
    Base serializer for the Combination model.
    """
    class Meta:
        model = Combination
        fields = '__all__'  
        