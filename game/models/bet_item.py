from django.db import models
from .bet_transaction import BetTransaction
from .combination import Combination
from .base import TimeStampedModel


class BetItem(TimeStampedModel):
    """
    This model represents a bet item for a bet transaction.
    """
    
    id = models.AutoField(primary_key=True)
    bet_transaction = models.ForeignKey(BetTransaction, on_delete=models.CASCADE, related_name="bet_items")
    combination = models.ForeignKey(Combination, on_delete=models.CASCADE, related_name="bet_items")
    straightAmount = models.DecimalField(max_digits=10, decimal_places=2)
    rumbleAmount = models.DecimalField(max_digits=10, decimal_places=2)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"BetItem {self.id} - Transaction {self.bet_transaction.id} - Amount {self.amount}"
