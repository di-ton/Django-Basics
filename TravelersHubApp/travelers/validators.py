import re

from django.core.exceptions import ValidationError



def nickname_validator(value):
    regex = "^[a-zA-Z0-9]+$"
    if not re.match(regex, value):
        raise ValidationError("Your nickname is invalid!")

