from django import forms

from common.mixins import ReadOnlyMixin
from pets.models import Pet


class PetBaseForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Pet
        fields = ['name', 'date_of_birth', 'personal_photo']

        labels = {
            "name": "Pet Name:",
            "date_of_birth": "Date of Birth:",
            "personal_photo": "Link to image:",
        }

        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Pet name"}),
            # "date_of_birth": forms.DateInput(
            #     attrs={"type": "date"}),
            "personal_photo": forms.TextInput(attrs={"placeholder": "Link to image"}),
        }


class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(PetBaseForm):
    pass


class PetDeleteForm(ReadOnlyMixin, PetBaseForm):
    pass































