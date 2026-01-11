from django.core.validators import MinLengthValidator
from django.db import models

from profiles.validators import name_validator


class Profile(models.Model):
    nickname = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(2)],
        unique=True,
        error_messages={"min_length": "Nickname must be at least 2 chars long!"}
    )
    first_name = models.CharField(
        max_length=30,
        validators=[name_validator],
    )
    last_name = models.CharField(
        max_length=30,
        validators=[name_validator],
    )
    chef = models.BooleanField(default=False)
    bio = models.TextField(blank=True, null=True)

