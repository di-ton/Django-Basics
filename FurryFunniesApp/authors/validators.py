import re

from django.core.exceptions import ValidationError



def name_validator(value):
    regex = "^[a-zA-Z]+$"
    if not re.match(regex, value):
        raise ValidationError("Your name must contain letters only!")


def password_validator(value):
    if not len(value) == 6 or not value.isdigit():
        raise ValidationError("Your passcode must be exactly 6 digits!")