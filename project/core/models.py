import logging
import uuid

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models

from autoslug import AutoSlugField
from dirtyfields import DirtyFieldsMixin
from phonenumber_field.modelfields import PhoneNumberField

from dirtyfields import DirtyFieldsMixin
from address.models import AddressField

from common.lists import COUNTRIES

from .managers import CustomUserManager
from .utils import get_user_slug
from .choices import (
    UserGender,
    UserStatus,
    UserKind,
    UserType,
    UserTheme,
)


logger = logging.getLogger(__name__)


class User(AbstractUser, DirtyFieldsMixin):
    """
    A custom User class that inherits from AbstractUser and BaseModelWithUID.

    This class combines features from multiple Django base classes to create a custom user model
    with additional functionality. It includes DirtyFieldsMixin for tracking changed fields,
    AbstractUser for core user attributes, and PermissionsMixin for managing user permissions.

    Attributes:
        Inherits attributes and methods from DirtyFieldsMixin, AbstractUser, and BaseModelWithUID.

    Example usage:
        user = User.objects.create(username='wazed_khan', email='wazedkhan111024@example.com')
        user.set_password('123456')
        user.save()
    """  # noqa: E501

    uid = models.UUIDField(
        default=uuid.uuid4, editable=False, db_index=True, unique=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    phone = PhoneNumberField(db_index=True, unique=True, blank=False, null=True)
    email = models.EmailField(db_index=True, unique=True, blank=False)
    country = models.CharField(
        max_length=2, choices=COUNTRIES, default="bd", db_index=True
    )
    language = models.CharField(max_length=2, default="en")
    slug = AutoSlugField(populate_from=get_user_slug, unique=True, db_index=True)
    gender = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        choices=UserGender.choices,
        db_index=True,
    )
    status = models.CharField(
        max_length=20,
        choices=UserStatus.choices,
        db_index=True,
        default=UserStatus.DRAFT,
    )
    date_of_birth = models.DateField(null=True, blank=True)

    # extra fields for User model from existing e_com-backend's Person model
    code = models.CharField(blank=True, null=True, max_length=16, unique=True)
    nid = models.CharField(
        max_length=32,
        default=None,
        blank=True,
        null=True,
        verbose_name="NID No",
        help_text="National ID No",
    )
    user_kind = models.CharField(
        max_length=50,
        choices=UserKind.choices,
        default=UserKind.USER,
        db_index=True,
    )
    user_type = models.CharField(
        max_length=50,
        choices=UserType.choices,
        default=UserType.EXTERNAL,
        db_index=True,
    )
    theme = models.CharField(
        max_length=50, choices=UserTheme.choices, default=UserTheme.LIGHT, db_index=True
    )

    address = AddressField(blank=True, null=True, on_delete=models.SET_NULL)

    objects = CustomUserManager()

    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ("-date_joined",)

    def __str__(self) -> str:
        return f"ID: {self.id}, {self.get_name()},  Phone: {self.phone}"

    def get_name(self):
        name = " ".join([self.first_name, self.last_name])
        return name.strip()
