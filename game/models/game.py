from django.db import models
from .base import TimeStampedModel

class Game(TimeStampedModel):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=False)
    digits = models.IntegerField(default=3)

    def __str__(self):
        return self.name