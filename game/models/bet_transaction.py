from django.db import models
from .base import TimeStampedModel
from .game_schedules import GameSchedule

class BetTransaction(TimeStampedModel):
    """
    This model represents a bet transaction for a game.
    """
    
    id = models.AutoField(primary_key=True)
    game_schedule = models.ForeignKey(GameSchedule, on_delete=models.CASCADE, related_name="bet_transactions")
    user_id = models.BigIntegerField()
    transactionType = models.IntegerField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"BetTransaction {self.id} - User {self.user_id} - Amount {self.bet_amount}"