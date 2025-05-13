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