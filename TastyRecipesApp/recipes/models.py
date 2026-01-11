from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from recipes.choices import CuisineTypeChoices


class Recipe(models.Model):
    title = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(10)],
        unique=True,
        error_messages={
            "unique": "We already have a recipe with the same title!"
        }
    )
    cuisine_type = models.CharField(
        max_length=7,
        choices=CuisineTypeChoices.choices,
    )
    ingredients = models.TextField(
        help_text="Ingredients must be separated by a comma and space."
    )
    instructions = models.TextField()
    cooking_time = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Provide the cooking time in minutes."
    )
    image_url = models.URLField(blank=True, null=True)
    author = models.ForeignKey(
        "profiles.Profile",
        on_delete=models.CASCADE,
        related_name="recipes",
        editable=False,
    )

    @property
    def ingredients_list(self):
        return [ingredient.strip() for ingredient in self.ingredients.split(",")]




