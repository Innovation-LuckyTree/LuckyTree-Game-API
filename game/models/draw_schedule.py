from django.db import models
from .base import AuditedModel
from .company_game import CompanyGame

class DrawSchedule(AuditedModel):
    """
    This model represents the types of draws for each game.
    note: set time to epoch time in milliseconds
    """
    
    id = models.AutoField(primary_key=True)
    company_game = models.ForeignKey(CompanyGame, on_delete=models.CASCADE, related_name="draw_schedules")
    name = models.CharField(max_length=255, default="DrawSchedule")
    cutoff_time = models.BigIntegerField()
    open_time = models.BigIntegerField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.game.title} - {self.draw_time}"