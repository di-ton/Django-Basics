from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from cars.choices import TypeChoices
from cars.validators import validate_year


class Car(models.Model):
    type = models.CharField(max_length=10, choices=TypeChoices.choices)
    model = models.CharField(max_length=15, validators=[MinLengthValidator(1)])
    year = models.IntegerField(validators=[validate_year])
    image_url = models.URLField(
        unique=True,
        error_messages={
            "unique": "This image URL is already in use! Provide a new one."
        }
    )
    price = models.FloatField(validators=[MinValueValidator(1.0)])
    owner = models.ForeignKey(
        "profiles.Profile",
        on_delete=models.CASCADE,
        related_name="cars",
        editable=False
    )
