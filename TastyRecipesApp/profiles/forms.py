from django import forms

from profiles.models import Profile


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["nickname", "first_name", "last_name", "chef"]
        labels = {
            "nickname": "Nickname:",
            "first_name": "First Name:",
            "last_name": "Last Name:",
            "chef": "Chef:",
        }

class EditProfileForm(ProfileCreateForm):
    class Meta(ProfileCreateForm.Meta):
        fields = ["nickname", "first_name", "last_name", "chef", "bio"]

        labels = {
            # "nickname": "Nickname:",
            # "first_name": "First Name:",
            # "last_name": "Last Name:",
            # "chef": "Chef:",
            "bio": "Bio:",
        }