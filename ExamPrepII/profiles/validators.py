from django.core.validators import RegexValidator

starts_with_letter = RegexValidator(
    regex=r'^[^\W\d_].*',
    message='Must start with a letter.'
)