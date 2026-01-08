from django import forms

from authors.models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ("first_name", "last_name", "pets_number", "passcode")

        labels = {
            "first_name": "First Name:",
            "last_name": "Last Name:",
            "pets_number": "Pet Number:",
            "passcode": "Password:",
        }
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "Enter your first name..."}),
            "last_name": forms.TextInput(attrs={"placeholder": "Enter your last name..."}),
            "passcode": forms.PasswordInput(attrs={"placeholder": "Enter 6 digits..."}),
            "pets_number": forms.TextInput(attrs={"placeholder": "Enter the number of your pets..."}),
        }


class AuthorEditForm(AuthorForm):
    class Meta(AuthorForm.Meta):
        fields = ("first_name", "last_name", "pets_number", "info", "image_url")
        labels = {
            "first_name": "First Name:",
            "last_name": "Last Name:",
            "pets_number": "Pet Number:",
            "info": "Info:",
            "image_url": "Profile Image URL:",
        }
