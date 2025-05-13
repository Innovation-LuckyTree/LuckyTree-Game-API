from rest_framework import serializers
from game.models import DrawSchedule

class BaseDrawScheduleSerializer(serializers.ModelSerializer):
    """
    Serializer for the DrawSchedule model.
    """
    class Meta:
        model = DrawSchedule
        fields = '__all__'  
        extra_kwargs = {
            'is_deleted': {'read_only': True},
        }
        