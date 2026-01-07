from django import forms

from fruits.models import Fruit


class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        exclude = ('owner',)
        labels = {
            'name': '',
            'image_url': '',
            'description': '',
            'nutrition': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Fruit Name',
            }),
            'image_url': forms.URLInput(attrs={
                'placeholder': 'Fruit Image URL',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Fruit Description',
            }),
            'nutrition': forms.Textarea(attrs={
                'placeholder': 'Nutrition Info',
            }),
        }

class CreateFruitForm(FruitBaseForm):
    pass

class EditFruitForm(FruitBaseForm):
    class Meta(FruitBaseForm.Meta):
        labels = {
            'name': 'Name:',
            'image_url': 'Image URL:',
            'description': 'Description:',
            'nutrition': 'Nutrition:',
        }

class DeleteFruitForm(FruitBaseForm):
    class Meta(FruitBaseForm.Meta):
        fields = ('name', 'image_url', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.disabled = True


# class DeleteFruitForm(forms.ModelForm):
#     class Meta:
#         model = Fruit
#         fields = ('name', 'image_url', 'description')
#         labels = {
#             'name': 'Name:',
#             'image_url': 'Image URL:',
#             'description': 'Description:',
#         }
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in self.fields.values():
#             field.disabled = True

class DetailsFruitForm(forms.Form):
    pass