from rest_framework import serializers
from game.models import Result

class BaseResultSerializer(serializers.ModelSerializer):
    """
    Base serializer for the Result model.
    """
    class Meta:
        model = Result
        fields = '__all__'
        extra_kwargs = {
            'is_deleted': {'read_only': True},
        }