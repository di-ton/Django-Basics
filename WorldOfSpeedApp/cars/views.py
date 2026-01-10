from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from cars.forms import CarCreateForm, CarEditForm, CarDeleteForm
from cars.models import Car
from common.utils import get_profile


# class CatalogueView(ListView):
#     model = Car
#     template_name = "catalogue.html"
#     context_object_name = "cars"
#     paginate_by = 3
#
#     def get_queryset(self):
#         return Car.objects.filter(owner=get_profile())

def catalogue_view(request):
    profile = get_profile()
    cars = Car.objects.filter(owner=profile)
    context = {'profile': profile, "cars": cars}
    return render(request, "catalogue.html", context)

class CreateCarView(CreateView):
    model = Car
    template_name = "car-create.html"
    success_url = reverse_lazy("catalogue")
    form_class = CarCreateForm

    def form_valid(self, form):
        form.instance.owner = get_profile()
        return super().form_valid(form)


class DetailsCarView(DetailView):
    model = Car
    template_name = "car-details.html"
    context_object_name = "car"
    pk_url_kwarg = "car_id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["owner"] = get_profile()
        return context

class DeleteCarView(UpdateView):
    model = Car
    template_name = "car-delete.html"
    pk_url_kwarg = "car_id"
    context_object_name = "car"
    success_url = reverse_lazy("catalogue")
    form_class = CarDeleteForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["owner"] = get_profile()
        return context


    def form_valid(self, form):
        self.object.delete()
        return redirect(self.success_url)

class EditCarView(UpdateView):
    model = Car
    template_name = "car-edit.html"
    success_url = reverse_lazy("catalogue")
    context_object_name = "car"
    pk_url_kwarg = "car_id"
    form_class = CarEditForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["owner"] = get_profile()
        return context