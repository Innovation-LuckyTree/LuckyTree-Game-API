from rest_framework import serializers
from game.models import Winner

class BaseWinnerSerializer(serializers.ModelSerializer):
    """
    Base serializer for the Winner model.
    """
    class Meta:
        model = Winner
        fields = '__all__'