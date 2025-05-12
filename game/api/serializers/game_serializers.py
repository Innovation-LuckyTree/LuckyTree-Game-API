from rest_framework import serializers
from game.models import Game

class BaseGameSerializer(serializers.ModelSerializer):
    """
    Base serializer for the Game model.
    """
    class Meta:
        model = Game
        fields = '__all__'  
        