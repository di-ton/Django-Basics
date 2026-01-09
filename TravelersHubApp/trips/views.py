from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from common.utilis import get_profile
from travelers.models import Traveler
from trips.forms import CreateTripForm, EditTripForm, DeleteTripForm
from trips.models import Trip


class TripCreateView(CreateView):
    model = Trip
    template_name = "create-trip.html"
    success_url = reverse_lazy("all-trips")
    form_class = CreateTripForm

    def form_valid(self, form):
        form.instance.traveler = get_profile()
        return super().form_valid(form)

class TripDetailsView(DetailView):
    model = Trip
    template_name = "details-trip.html"
    pk_url_kwarg = "trip_id"
    context_object_name = "trip"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["traveler"] = get_profile()
        return context


class TripEditView(UpdateView):
    model = Trip
    template_name = "edit-trip.html"
    success_url = reverse_lazy("all-trips")
    pk_url_kwarg = "trip_id"
    context_object_name = "trip"
    form_class = EditTripForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["traveler"] = get_profile()
        return context


class TripDeleteView(UpdateView):
    model = Trip
    template_name = "delete-trip.html"
    pk_url_kwarg = "trip_id"
    context_object_name = "trip"
    success_url = reverse_lazy("all-trips")
    form_class = DeleteTripForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["traveler"] = get_profile()
        return context


    def form_valid(self, form):
        self.object.delete()
        return redirect(self.success_url)