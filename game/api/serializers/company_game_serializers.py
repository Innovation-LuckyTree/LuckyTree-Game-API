from rest_framework import serializers
from game.models import CompanyGame

class BaseCompanyGameSerializer(serializers.ModelSerializer):
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
    
class GameMechanicsSerializer(serializers.Serializer):
    """
    Serializer for the game mechanics.
    """
    winAmount = serializers.IntegerField()
    straightLimit = serializers.IntegerField()
    rumbleLimit = serializers.IntegerField()