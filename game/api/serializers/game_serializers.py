from rest_framework import serializers
from game.models import Game

#GAME MECHANICS
class GameMechanicsSerializer(serializers.Serializer):
    """
    Serializer for the game mechanics.
    """
    winAmount = serializers.IntegerField()
    straightLimit = serializers.IntegerField()
    rumbleLimit = serializers.IntegerField()


class BaseGameSerializer(serializers.ModelSerializer):
    """
    Base serializer for the Game model.
    """
    default_mechanics = GameMechanicsSerializer()
    class Meta:
        model = Game
        fields = '__all__'  
        extra_kwargs = {
            'is_deleted': {'read_only': True},
        }
        
    def validate(self, data):
        game_mechanics = data.get('default_mechanics', {})
        winAmount = game_mechanics.get('winAmount')
        straightLimit = game_mechanics.get('straightLimit')
        rumbleLimit = game_mechanics.get('rumbleLimit')

        if winAmount is None:
            raise serializers.ValidationError("winAmount attribute in winAmount is required")
        if straightLimit is None:
            raise serializers.ValidationError("straightLimit attribute in winAmount is required")
        if rumbleLimit is None:
            raise serializers.ValidationError("rumbleLimit attribute in gameMechanics is required")

        return data
    

class SimpleGameSerializer(serializers.ModelSerializer):
    """
    Serializer for the Game model with only the name field.
    """
    gameId = serializers.IntegerField(source='id')
    gameName = serializers.CharField(source='name')
    class Meta:
        model = Game
        fields = ['gameId', 'gameName', 'digits']
        
        