from django.db import models
from .base import AuditedModel
from .game import Game

class CompanyGame(AuditedModel):
    """
    mechanics Structure: {
        "winAmount": int,
        "straightLimit": int,
        "rumbleLimit": int
    }
    """
    
    def game_mechanics_default():
        return {"winAmount": 600, "straightLimit": 200, "rumbleLimit": 200}

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    company_id = models.UUIDField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="company_games")
    description = models.TextField()
    is_playable = models.BooleanField(default=True)
    mechanics = models.JSONField("Game Mechanics", default=game_mechanics_default)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title