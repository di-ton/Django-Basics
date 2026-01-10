from django.core.validators import RegexValidator


class UsernameValidator(RegexValidator):
    regex = r'^[A-Za-z0-9_]+$'
    message = "Username must contain only letters, digits, and underscores!"