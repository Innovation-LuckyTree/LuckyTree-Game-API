from rest_framework import serializers
from game.models import GameSchedule

class BaseGameScheduleSerializer(serializers.ModelSerializer):
    """
    Serializer for the GameSchedule model.
    """
    class Meta:
        model = GameSchedule
        fields = '__all__'  
        extra_kwargs = {
            'is_deleted': {'read_only': True},
        }

class CreateGameScheduleRequest(serializers.ModelSerializer):
    class Meta:
        model = GameSchedule
        fields = ('created_by', 'date', 'status', 'draw_schedule')

    def create(self, validated_data):
        validated_data['updated_by'] = validated_data['created_by']
        return GameSchedule.objects.create(**validated_data)