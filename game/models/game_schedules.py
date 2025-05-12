from django.db import models
from .base import AuditedModel
from .company_game import CompanyGame
from .draw_schedule import DrawSchedule

class GameSchedule(AuditedModel):
    """
    Represents a draw_schedule of a game in a specific date.
    notes:
        Status: 0: inactive, 1: active
        - if status is 0 but allow advanced is true, it means that the schedule is inactive but can still be used for advanced betting.
    """
    id = models.AutoField(primary_key=True)
    company_game = models.ForeignKey(CompanyGame, on_delete=models.CASCADE, related_name="schedules")
    draw_schedule = models.ForeignKey(DrawSchedule, on_delete=models.CASCADE, related_name="schedules")
    date = models.BigIntegerField()
    allow_advanced = models.BooleanField(default=True)
    status = models.IntegerField(default=True) # 0: inactive, 1: active, 2:closed/waiting for results
    is_deleted = models.BooleanField(default=False)
    win_amount = models.IntegerField(default=0)
    straight_limit = models.IntegerField(default=0)
    rumble_limit = models.IntegerField(default=0)
    scheduleName = models.CharField(max_length=255)
    cutoff_time = models.BigIntegerField()
    open_time = models.BigIntegerField()

    def __str__(self):
        return f"{self.game.title} - {self.schedule_time}"