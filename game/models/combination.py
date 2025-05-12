from django.db import models

class Combination(models.Model):
    """
    Represents a combination of 3-digits (0-1) ex. 1-2-0.
    """
    id = models.AutoField(primary_key=True)
    value = models.CharField(max_length=5)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"Combination {self.value}"