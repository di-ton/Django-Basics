from django import forms

from profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'password')

        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name',
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last Name',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email',
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Password',
            }),
        }
        help_texts = {
            'password': '*Password length requirements: 8 to 20 characters',
        }

class CreateProfileForm(ProfileBaseForm):
    pass
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     for field in self.fields.values():
    #         field.required = False
    #
    # def clean(self):
    #     cleaned_data = super().clean()
    #
    #     if not cleaned_data.get('first_name'):
    #         raise forms.ValidationError('')
    #
    #     if not cleaned_data.get('last_name'):
    #         raise forms.ValidationError('')
    #
    #     if not cleaned_data.get('email'):
    #         raise forms.ValidationError('')
    #
    #     if not cleaned_data.get('password'):
    #         raise forms.ValidationError('')
    #
    #     return cleaned_data




class DetailsProfileForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        labels = {
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'email': 'Email:',
            'age': 'Age:',
            'image_url': 'Image URL:',
        }


class EditProfileForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        fields = ('first_name', 'last_name', 'image_url', 'age')
        labels = {
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'image_url': 'Image URL:',
            'age': 'Age:',
        }





