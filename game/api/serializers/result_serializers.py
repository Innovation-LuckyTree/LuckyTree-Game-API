from rest_framework import serializers
from game.models import Result, Combination, Winner, BetItem
from itertools import permutations
from django.db import transaction
from decimal import Decimal
from .winner_serializers import SimpleWinnerSerializer


class BaseResultSerializer(serializers.ModelSerializer):
    """
    Base serializer for the Result model.
    """
    combination = serializers.CharField(source='combination.value')
    winners = SimpleWinnerSerializer(read_only=True, many=True)
    no_of_winners = serializers.SerializerMethodField()
    class Meta:
        model = Result
        fields = '__all__'
        extra_kwargs = {
            'is_deleted': {'read_only': True},
        }
        
    def get_no_of_winners(self, obj):
        return obj.winners.count()


class SimpleCreateResultSerializer(serializers.ModelSerializer):
    combination = serializers.CharField() 
    class Meta:
        model = Result
        fields=('combination', 'game_schedule', 'created_by')
        
    def validate(self, data):
        game_schedule = data.get('game_schedule')

        if Result.objects.filter(game_schedule=game_schedule, is_deleted=False).exists():
            raise serializers.ValidationError("A result already exists for this game schedule.")

        return data
    
    def validate_combination(self, value):
        try:
            return Combination.objects.get(value=value)
        except Combination.DoesNotExist:
            raise serializers.ValidationError(f"Combination '{value}' does not exist.")

    def create(self, validated_data):
        with transaction.atomic():
            result = Result.objects.create(**validated_data)
            winning_value = result.combination.value

            rumble_matches = self.generate_rumble_variants(winning_value)

            matching_bet_items = BetItem.objects.filter(
                bet_transaction__game_schedule=result.game_schedule,
                combination__value__in=rumble_matches,
                is_deleted=False
            )

            winners = [
                Winner(
                    bet_item=item, 
                    result=result, 
                    win_amount=item.straightAmount*result.game_schedule.win_amount if result.combination == item.combination else 0,
                    rumble_amount=item.straightAmount*Decimal(str(result.game_schedule.win_amount/len(rumble_matches))),
                )
                for item in matching_bet_items
            ]

            Winner.objects.bulk_create(winners)
            return result
    
    def generate_rumble_variants(self, value: str):
        digits = value.split('-') 
        perms = set(permutations(digits))
        return set('-'.join(p) for p in perms)