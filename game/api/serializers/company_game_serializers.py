from rest_framework import serializers
from game.api.serializers import  SimpleGameSerializer, GameMechanicsSerializer
from game.models import CompanyGame

class BaseCompanyGameSerializer(serializers.ModelSerializer):
    """
    Base serializer for the CompanyGame model.
    """
    class Meta:
        model = CompanyGame
        fields = '__all__'  
        extra_kwargs = {
            'is_deleted': {'read_only': True},
        }
        
    def validate(self, data):
        game_mechanics = data.get('mechanics', None)
        if game_mechanics is not None:
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
    

class SimpleCompanyGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyGame
        fields = ['id', 'title', 'description', 'is_playable','game','updated_by', 'updated_at', 'updated_property']

    
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
    