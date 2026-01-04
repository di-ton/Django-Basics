from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from profiles.validators import UsernameValidator


class Profile(models.Model):
    username = models.CharField(max_length=15, validators=[
        MinLengthValidator(2),
        UsernameValidator(),
    ])

    email = models.EmailField()
    age = models.IntegerField(validators=[MinValueValidator(0)], blank=True, null=True)

