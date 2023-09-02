from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from address.models import AddressField

from common.models import BaseModelWithUUIDStatus
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin, BaseModelWithUUIDStatus):
    address = AddressField(blank=True, null=True, on_delete=models.SET_NULL)
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
