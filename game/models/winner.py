from django.db import models
from .base import TimeStampedModel
from .bet_item import BetItem
from .result import Result

class Winner(TimeStampedModel):
    """
    This model represents the winner of a game.
    """
    
    id = models.AutoField(primary_key=True)
    bet_item = models.ForeignKey(BetItem, on_delete=models.CASCADE, related_name="winners")
    result = models.ForeignKey(Result, on_delete=models.CASCADE, related_name="winners")
    win_amount = models.DecimalField(max_digits=10, decimal_places=2)
    rumble_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"Winner {self.id} - Bet Item {self.bet_item.id} - Result {self.result.id}"