

from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from common.utils import get_profile
from profiles.forms import ProfileCreateForm, EditProfileForm
from profiles.models import Profile




class CreateProfileView(CreateView):
    model = Profile
    template_name = "create-profile.html"
    success_url = reverse_lazy("catalogue")
    form_class = ProfileCreateForm


class DetailProfileView(DetailView):
    model = Profile
    template_name = "details-profile.html"
    pk_url_kwarg = "pk"
    context_object_name = "profile"


class EditProfileView(UpdateView):
    model = Profile
    template_name = "edit-profile.html"
    pk_url_kwarg = "pk"
    context_object_name = "profile"
    form_class = EditProfileForm

    def get_success_url(self):
        return reverse("details-profile", kwargs={
            "pk": self.object.pk
        })


class DeleteProfileView(DeleteView):
    model = Profile
    template_name = "delete-profile.html"
    pk_url_kwarg = "pk"
    context_object_name = "profile"
    success_url = reverse_lazy("home")

    def post(self, request, *args, **kwargs):
        profile = get_profile()
        if profile:
            profile.delete()
        return redirect(self.success_url)

    # def post(self, request, *args, **kwargs):
    #     Profile.objects.all().delete()
    #     return redirect(self.success_url)




