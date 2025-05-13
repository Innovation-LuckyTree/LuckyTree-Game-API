from .base_serializer import BaseModelSerializer
from game.models import Game

class BaseGameSerializer(BaseModelSerializer):
    """
    Base serializer for the Game model.
    """
    class Meta:
        model = Game
        fields = '__all__'  

class SimpleGameSerializer(BaseModelSerializer):
    """
    Serializer for the Game model with only the name field.
    """
    class Meta:
        model = Game
        fields = ['id', 'name', 'digits']
        