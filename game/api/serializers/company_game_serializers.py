from rest_framework import serializers
from game.api.serializers import BaseModelSerializer, SimpleGameSerializer
from game.models import CompanyGame

class BaseCompanyGameSerializer(BaseModelSerializer):
    """
    Base serializer for the CompanyGame model.
    """
    class Meta:
        model = CompanyGame
        fields = '__all__'  
        
    def validate(self, data):
        game_mechanics = data.get('mechanics', {})
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
    

class SimpleCompanyGameSerializer(BaseModelSerializer):
    """
    Serializer for the Game model with only the name field.
    """
    class Meta:
        model = CompanyGame
        fields = ['id', 'title', 'description', 'is_playable','game','updated_by', 'updated_at', 'updated_property']


class GameMechanicsSerializer(serializers.Serializer):
    """
    Serializer for the game mechanics.
    """
    winAmount = serializers.IntegerField()
    straightLimit = serializers.IntegerField()
    rumbleLimit = serializers.IntegerField()

    
class CompanyGameListSerializer(BaseCompanyGameSerializer):
    """
    Serializer for listing CompanyGame instances.
    """
    game = SimpleGameSerializer(read_only=True)

    
class UpdateRequestSerializer(GameMechanicsSerializer):
    updated_by = serializers.IntegerField()


class GameDetailsUpdateRequest(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    is_playable = serializers.BooleanField()
    