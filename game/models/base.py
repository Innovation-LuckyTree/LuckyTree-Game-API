from django.db import models
from django.utils import timezone

"""
Base models for our Tables (TimeStamed, Auditable, etc.)
"""

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AuditedModel(TimeStampedModel):
    created_by = models.BigIntegerField(null=True)
    updated_by = models.BigIntegerField(null=True)
    updated_property = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        abstract = True