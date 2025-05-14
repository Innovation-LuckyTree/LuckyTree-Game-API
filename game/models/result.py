from django.db import models
from .base import AuditedModel
from .game_schedules import GameSchedule
from .combination import Combination

class Result(AuditedModel):
    """
    Represents the result of a game.
    STATUS - 0 for pending, 1 for confirmed, 2 for declined
    """
    id = models.AutoField(primary_key=True)
    game_schedule = models.ForeignKey(GameSchedule, on_delete=models.CASCADE, related_name="results")
    combination = models.ForeignKey(Combination, on_delete=models.CASCADE, related_name="results")
    status = models.IntegerField(default=0) #0-pending, 1-confirmed, 2 for declined
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"Result {self.id} - Game Schedule {self.game_schedule.id} - Combination {self.combination.value}"