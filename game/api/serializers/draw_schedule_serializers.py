from rest_framework import serializers
from game.models import DrawSchedule

class BaseDrawScheduleSerializer(serializers.ModelSerializer):
    """
    Serializer for the DrawSchedule model.
    """
    class Meta:
        model = DrawSchedule
        fields = '__all__'  