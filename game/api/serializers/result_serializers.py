from rest_framework import serializers
from game.models import Result, Combination

class BaseResultSerializer(serializers.ModelSerializer):
    """
    Base serializer for the Result model.
    """
    combination = serializers.CharField(source='combination.value')
    class Meta:
        model = Result
        fields = '__all__'
        extra_kwargs = {
            'is_deleted': {'read_only': True},
        }

class SimpleCreateResultSerializer(serializers.ModelSerializer):
    combination = serializers.CharField() 
    class Meta:
        model = Result
        fields=('combination', 'game_schedule', 'created_by')
        
    def validate_combination(self, value):
        try:
            return Combination.objects.get(value=value)
        except Combination.DoesNotExist:
            raise serializers.ValidationError(f"Combination '{value}' does not exist.")

    def create(self, validated_data):
        validated_data['updated_by'] = validated_data['created_by']
        return Result.objects.create(**validated_data)