from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, FormView

from fruits.forms import CreateFruitForm, EditFruitForm, DeleteFruitForm
from fruits.models import Fruit
from profiles.models import Profile


class CreateFruitView(CreateView):
    model = Fruit
    form_class = CreateFruitForm
    template_name = "create-fruit.html"
    success_url = reverse_lazy('dashboard')

    def dispatch(self, request, *args, **kwargs):
        if not Profile.objects.exists():
            return redirect('create-profile')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        fruit = form.save(commit=False)
        fruit.owner = Profile.objects.first()  # assign owner
        fruit.save()
        print("Saving fruit:", form.cleaned_data)
        return super().form_valid(form)


class DetailsFruitView(DetailView):
    model = Fruit
    template_name = "details-fruit.html"
    pk_url_kwarg = 'pk'
    context_object_name = 'fruit'


class EditFruitView(UpdateView):
    model = Fruit
    form_class = EditFruitForm
    template_name = "edit-fruit.html"
    pk_url_kwarg = 'pk'
    context_object_name = 'fruit'
    success_url = reverse_lazy("dashboard")

class DeleteFruitView(DeleteView):
    model = Fruit
    template_name = "delete-fruit.html"
    # form_class = DeleteFruitForm
    success_url = reverse_lazy("dashboard")
    pk_url_kwarg = 'pk'
    context_object_name = 'fruit'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DeleteFruitForm(instance=self.object)
        return context


    # def dispatch(self, request, *args, **kwargs):
    #     self.fruit = get_object_or_404(Fruit, pk=kwargs['pk'])
    #     return super().dispatch(request, *args, **kwargs)
    #
    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs['instance'] = self.fruit
    #     return kwargs
    #
    # def form_valid(self, form):
    #     self.fruit.delete()
    #     return super().form_valid(form)



