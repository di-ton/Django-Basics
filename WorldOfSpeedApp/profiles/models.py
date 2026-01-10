from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.db.models import Sum

from profiles.validators import UsernameValidator


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(3, message="Username must be at least 3 chars long!"),
            UsernameValidator
        ]
    )
    email = models.EmailField()
    age = models.IntegerField(
        validators=[MinValueValidator(21)],
        help_text="Age requirement: 21 years and above."
    )
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=25, blank=True, null=True)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    profile_picture = models.URLField(blank=True, null=True)

    @property
    def total_car_price(self):
        return self.cars.aggregate(total=Sum("price"))["total"] or 0












