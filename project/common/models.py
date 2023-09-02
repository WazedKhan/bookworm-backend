import uuid

from django.db import models

from dirtyfields import DirtyFieldsMixin

from .choices import InstanceStatus


class BaseModelWithUUIDStatus(DirtyFieldsMixin, models.Model):
    uid = models.UUIDField(
        db_column=True, unique=True, default=uuid.uuid4, editable=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=50,
        choices=InstanceStatus.choices,
        db_index=True,
        default=InstanceStatus.ACTIVE,
    )

    class Meta:
        abstract = True
        ordering = [
            "-created_at",
        ]
