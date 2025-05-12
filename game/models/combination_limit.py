from django.db import models
from .base import AuditedModel
from .combination import Combination

class CombinationLimit(AuditedModel):
    """
    Represents the limit of a combination in a game.
    """
    id = models.AutoField(primary_key=True)
    combination = models.ForeignKey(Combination, on_delete=models.CASCADE, related_name="limits")
    straight_limit = models.IntegerField()
    rumble_limit = models.IntegerField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"CombinationLimit {self.id} - Combination {self.combination.value}"