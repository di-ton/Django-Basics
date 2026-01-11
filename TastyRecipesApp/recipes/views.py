from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from common.utils import get_profile
from recipes.forms import CreateRecipeForm, DeleteRecipeForm
from recipes.models import Recipe


def catalogue_view(request):
    profile = get_profile()
    recipes = Recipe.objects.filter(author=profile)
    context = {'profile': profile, "recipes": recipes}
    return render(request, "catalogue.html", context)


class CreateRecipeView(CreateView):
    model = Recipe
    template_name = "create-recipe.html"
    form_class = CreateRecipeForm
    success_url = reverse_lazy("catalogue")

    def form_valid(self, form):
        form.instance.author = get_profile()
        return super().form_valid(form)


class DetailRecipeView(DetailView):
    model = Recipe
    template_name = "details-recipe.html"
    context_object_name = "recipe"
    pk_url_kwarg = "pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["author"] = get_profile()
        return context

class EditRecipeView(UpdateView):
    model = Recipe
    template_name = "edit-recipe.html"
    context_object_name = "recipe"
    pk_url_kwarg = "pk"
    success_url = reverse_lazy("catalogue")
    form_class = CreateRecipeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["author"] = get_profile()
        return context

class DeleteRecipeView(UpdateView):
    model = Recipe
    template_name = "delete-recipe.html"
    context_object_name = "recipe"
    pk_url_kwarg = "pk"
    success_url = reverse_lazy("catalogue")
    form_class = DeleteRecipeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["owner"] = get_profile()
        return context

    def form_valid(self, form):
        self.object.delete()
        return redirect(self.success_url)








