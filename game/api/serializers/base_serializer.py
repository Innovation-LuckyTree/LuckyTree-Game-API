from rest_framework import serializers

class BaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        fields = '__all__'
        extra_kwargs = {
            'is_deleted': {'read_only': True},
        }