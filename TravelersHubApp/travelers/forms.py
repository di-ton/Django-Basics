from django import forms

from travelers.models import Traveler


class TravelerForm(forms.ModelForm):
    class Meta:
        model = Traveler
        fields = "__all__"


class TravelerCreateForm(TravelerForm):
    class Meta(TravelerForm.Meta):
        fields = ["nickname", "email", "country"]
        labels = {
            "nickname": "Nickname:",
            "email": "Email:",
            "country": "Country:",
        }

        widgets = {
            "nickname": forms.TextInput(attrs={"placeholder": "Enter a unique nickname..."}),
            "email": forms.EmailInput(attrs={"placeholder": "Enter a valid email address..."}),
            "country": forms.TextInput(attrs={"placeholder": "Enter a country code like <BGR>..."}),
        }

class TravelerEditForm(TravelerForm):
    class Meta(TravelerForm.Meta):
        fields = ["nickname", "email", "country", "about_me"]
        labels = {
            "nickname": "Nickname:",
            "email": "Email:",
            "country": "Country:",
            "about": "About me:",
        }

        help_texts = {
            "nickname": "*Nicknames can contain only letters and digits.",
        }
