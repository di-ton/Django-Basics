from django import forms

from posts.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "image_url"]
        labels = {
            "title": "Title:",
            "content": "Content:",
            "image_url": "Post Image URL:",
        }
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Put an attractive and unique title..."}),
            "content": forms.TextInput(attrs={"placeholder": "Share some interesting facts about your adorable pets..."}),
        }

class PostCreateForm(PostBaseForm):
    pass


class PostEditForm(PostBaseForm):
    pass


class PostDeleteForm(PostBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["readonly"] = True