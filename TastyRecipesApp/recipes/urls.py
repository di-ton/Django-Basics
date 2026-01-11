from django.urls import path

from recipes import views
from recipes.forms import CreateRecipeForm
from recipes.views import catalogue_view, CreateRecipeView

urlpatterns = [
    path("catalogue/", catalogue_view, name="catalogue"),
    path("create/", views.CreateRecipeView.as_view(), name="create-recipe"),
    path("<int:pk>/details/", views.DetailRecipeView.as_view(), name="details-recipe"),
    path("<int:pk>/edit/", views.EditRecipeView.as_view(), name="edit-recipe"),
    path("<int:pk>/delete/", views.DeleteRecipeView.as_view(), name="delete-recipe"),
]