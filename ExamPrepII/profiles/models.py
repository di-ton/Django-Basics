from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models

from profiles.validators import starts_with_letter


class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
        validators=[
            MinLengthValidator(2),
            starts_with_letter,
        ]
    )
    last_name = models.CharField(
        max_length=35,
        validators=[
            MinLengthValidator(1),
            starts_with_letter,
        ]
    )
    email = models.EmailField(max_length=40, unique=True)
    password = models.CharField(
        max_length=20,
        validators=[
            MinLengthValidator(8),
        ],
        help_text="*Password length requirements: 8 to 20 characters"
    )
    image_url = models.URLField(
        null=True,
        blank=True,
    )
    age = models.IntegerField(default=18, blank=True, null=True)











