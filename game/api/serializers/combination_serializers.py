from rest_framework import serializers
from game.models import Combination

class CombinationSerializer(serializers.ModelSerializer):
    """
    Base serializer for the Combination model.
    """
    class Meta:
        model = Combination
        fields = '__all__'  
        extra_kwargs = {
            'is_deleted': {'read_only': True},
        }
        
class SimpleCombinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Combination
        fields = ('value', 'id')