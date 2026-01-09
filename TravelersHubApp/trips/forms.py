from travelers import forms
from django import forms

from trips.models import Trip


class TripBaseForm(forms.ModelForm):
    class Meta:
        model = Trip
        exclude = ('traveler',)

        labels = {
            "destination": "Destination:",
            "summary": "Summary:",
            "start_date": "Started on:",
            "duration": "Duration:",
            "image_url": "Image URL:",
        }

        help_texts = {
            "duration": "*Duration in days is expected.",
        }

        widgets = {
            "destination": forms.TextInput(attrs={
                "placeholder": "Enter a short destination note...",
            }),
            "summary": forms.Textarea(attrs={
                "placeholder": "Share your exciting moments...",
            }),
            "start_date": forms.DateInput(attrs={
                "type": "date",
            }),
            "duration": forms.NumberInput(attrs={
                "value": 1,
            }),
            "image_url": forms.URLInput(attrs={
                "placeholder": "An optional image URL...",
            }),
        }


class CreateTripForm(TripBaseForm):
    pass

class EditTripForm(TripBaseForm):
    pass

class DeleteTripForm(TripBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["readonly"] = True