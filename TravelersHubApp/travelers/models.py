from django.core.validators import MinLengthValidator
from django.db import models
from pyexpat.errors import messages

from travelers.validators import nickname_validator


class Traveler(models.Model):
    nickname = models.CharField(
        max_length=30,
        unique=True,
        validators=[
            MinLengthValidator(3),
            nickname_validator,
        ],
        help_text="*Nicknames can contain only letters and digits."
    )
    email = models.EmailField(unique=True, max_length=30)
    country = models.CharField(max_length=3, validators=[MinLengthValidator(3)])
    about_me = models.TextField(blank=True, null=True)
