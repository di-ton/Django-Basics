from django import forms

from albums.mixins import ReadOnlyMixin
from albums.models import Album

class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ['owner']

        widgets = {
            "album_name": forms.TextInput(attrs={"placeholder": "Album name"}),
            "artist": forms.TextInput(attrs={"placeholder": "Artist"}),
            "description": forms.TextInput(attrs={"placeholder": "Album description"}),
            "image_url": forms.TextInput(attrs={"placeholder": "Image URL"}),
            "price": forms.TextInput(attrs={"placeholder": "Price"}),
        }


class AlbumCreateForm(AlbumBaseForm):
    pass


class AlbumEditForm(AlbumBaseForm):
    pass


class AlbumDeleteForm(ReadOnlyMixin, AlbumBaseForm):
    pass

















