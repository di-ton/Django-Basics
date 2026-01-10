from django import forms

from cars.models import Car


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ("type", "model", "price", "year", "image_url")

        labels = {
            "type": "Type:",
            "model": "Model:",
            "price": "Price:",
            "year": "Year:",
            "image_url": "Image URL:",
        }

        widgets = {
            "image_url": forms.URLInput(attrs={"placeholder": "https://..."}),
        }

class CarCreateForm(CarBaseForm):
    pass

class CarEditForm(CarBaseForm):
    pass

class CarDeleteForm(CarBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["readonly"] = True