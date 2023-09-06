from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "uid",
        "first_name",
        "last_name",
        "email",
        "phone",
        "country",
    )
    list_filter = ("email", "last_name", "phone")
    search_fields = (
        "last_name__startswith",
        "first_name",
    )

    class Meta:
        ordering = ("last_name", "first_name")
