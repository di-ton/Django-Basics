from django.core.validators import MinLengthValidator
from django.db import models

from fruits.validators import only_letters_validator
from profiles.models import Profile


class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(3),
            only_letters_validator,
        ],
        unique=True,
        error_messages={
            'unique': 'This fruit name is already in use! Try a new one.',
        }
    )
    image_url = models.URLField()
    description = models.TextField()
    nutrition = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='fruits')







