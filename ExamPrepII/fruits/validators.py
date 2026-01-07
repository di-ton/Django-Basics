from django.core.validators import RegexValidator

only_letters_validator = RegexValidator(
    regex=r"^[a-zA-Z]+$",
    message="Fruit name should contain only letters!",
)