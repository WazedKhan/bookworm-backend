from django.db import models


class UserType(models.TextChoices):
    INTERNAL = "INTERNAL", "Internal"
    EXTERNAL = "EXTERNAL", "External"


class UserGender(models.TextChoices):
    MALE = "MALE", "Male"
    OTHER = "OTHER", "Other"
    FEMALE = "FEMALE", "Female"


class UserTheme(models.TextChoices):
    DARK = "DARK", "Dark"
    LIGHT = "LIGHT", "Light"


class UserKind(models.TextChoices):
    AD = "AD", "Ad"
    USER = "USER", "User"
    PUBLISHER = "PUBLISHER", "PUBLISHER"


class UserStatus(models.TextChoices):
    DRAFT = "DRAFT", "Draft"
    ACTIVE = "ACTIVE", "Active"
    HIDDEN = "HIDDEN", "Hidden"
    INACTIVE = "INACTIVE", "Inactive"


class PrivacyType(models.TextChoices):
    PUBLIC = "PUBLIC", "Public"
    PRIVATE = "PRIVATE", "Private"
