from django.db import models

class InstanceStatus(models.TextChoices):
    DRAFT = "DRAFT", "Draft"
    ACTIVE = "ACTIVE", "Active"
    HIDDEN = "HIDDEN", "Hidden"
    PAUSED = "PAUSED", "Paused"
    REMOVED = "REMOVED", "Removed"