from django import forms

from profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

class ProfileCreateForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        fields = ("username", "email", "age", "password")
        labels = {
            "username": "Username:",
            "email": "Email:",
            "age": "Age:",
            "password": "Password:",
        }


class ProfileEditForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        labels = {
            "username": "Username:",
            "email": "Email:",
            "age": "Age:",
            "password": "Password:",
            "first_name": "First Name:",
            "last_name": "Last Name:",
            "profile_picture": "Profile Picture:",
        }
