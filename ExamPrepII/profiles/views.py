from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from profiles.forms import CreateProfileForm, EditProfileForm
from profiles.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = 'create-profile.html'
    success_url = reverse_lazy('dashboard')

    def dispatch(self, request, *args, **kwargs):
        if Profile.objects.exists():
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'details-profile.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'profile'

    # def get_object(self, queryset=None):
    #     profile = Profile.objects.first()
    #     if not profile:
    #         raise Http404("No profile exists.")
    #     return profile



class EditProfileView(UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'edit-profile.html'

    def get_object(self, queryset=None):
        return Profile.objects.first()

    def get_success_url(self):
        return reverse_lazy('details-profile', kwargs={'pk': self.object.pk})


class DeleteProfileView(DeleteView):
    model = Profile
    template_name = 'delete-profile.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return Profile.objects.first()

    def post(self, request, *args, **kwargs):
        profile = self.get_object()
        profile.delete()   # deletes fruits via CASCADE
        return redirect(self.success_url)