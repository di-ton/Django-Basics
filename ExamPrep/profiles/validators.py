from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class UsernameValidator:
    def __init__(self, message: str = None) -> None:
        self.message = message


    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, value: str):
        if value is None:
            self.__message = "Ensure this value contains only letters, numbers, and underscore."
        else:
            self.__message = value

    def __call__(self, value: str):
        if not value.replace("_", "").isalnum():
            raise ValidationError(self.message)
