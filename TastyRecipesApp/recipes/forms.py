from django import forms

from recipes.models import Recipe


class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'ingredients', 'instructions', "cooking_time", "cuisine_type", "image_url")

        labels = {
            "title": "Title:",
            "cuisine_type": 'Cuisine type:',
            "ingredients": 'Ingredients:',
            "instructions": 'Instructions:',
            "cooking_time": 'Cooking time:',
            "image_url": 'Image URL:',
        }

        widgets = {
            'ingredients': forms.TextInput(
                attrs={
                    'placeholder': 'ingredient1, ingredient2, ...',
                }),
            'instructions': forms.Textarea(attrs={'placeholder': 'Enter detailed instructions here...'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Optional image URL here...'}),
        }


class DeleteRecipeForm(CreateRecipeForm):
    class Meta(CreateRecipeForm.Meta):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["readonly"] = True


