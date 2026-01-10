
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from profiles.forms import ProfileCreateForm, ProfileEditForm
from profiles.models import Profile


class CreateProfileView(CreateView):
    model = Profile
    template_name = "profile-create.html"
    success_url = reverse_lazy("catalogue")
    form_class = ProfileCreateForm

class DetailsProfileView(DetailView):
    model = Profile
    template_name = "profile-details.html"
    context_object_name = "profile"
    pk_url_kwarg = "pk"


class EditProfileView(UpdateView):
    model = Profile
    template_name = "profile-edit.html"
    context_object_name = "profile"
    form_class = ProfileEditForm

    def get_success_url(self):
        return reverse("profile-details", kwargs={
            "pk": self.object.pk
        })

class DeleteProfileView(DeleteView):
    model = Profile
    template_name = "profile-delete.html"
    context_object_name = "profile"
    pk_url_kwarg = "pk"
    success_url = reverse_lazy("index")




