from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from travelers.forms import TravelerCreateForm, TravelerEditForm
from travelers.models import Traveler


class CreateTravelerView(CreateView):
    model = Traveler
    template_name = "create-traveler.html"
    form_class = TravelerCreateForm
    success_url = reverse_lazy("all-trips")


class DetailsTravelerView(DetailView):
    model = Traveler
    template_name = "details-traveler.html"
    context_object_name = "traveler"
    pk_url_kwarg = "traveler_id"

class EditTravelerView(UpdateView):
    model = Traveler
    template_name = "edit-traveler.html"
    context_object_name = "traveler"
    pk_url_kwarg = "traveler_id"
    form_class = TravelerEditForm

    def get_success_url(self):
        return reverse("details-traveler", kwargs={
            "traveler_id": self.object.pk
        })

class DeleteTravelerView(DeleteView):
    model = Traveler
    template_name = "delete-traveler.html"
    context_object_name = "traveler"
    pk_url_kwarg = "traveler_id"
    success_url = reverse_lazy("index")








