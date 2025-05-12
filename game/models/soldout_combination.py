from django.db import models
from .base import AuditedModel
from .combination import Combination

class SoldoutCombination(AuditedModel):
    """
    Represents the limit of a combination in a game.
    """
    id = models.AutoField(primary_key=True)
    combination = models.ForeignKey(Combination, on_delete=models.CASCADE, related_name="soldouts")
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"SoldoutCombination {self.id} - Combination {self.combination.value}"