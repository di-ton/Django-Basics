from django.urls import path, include
from pets import views

urlpatterns = [
    # path("add/", views.pet_add_view, name="add-pet"),
path("add/", views.PetAddView.as_view(), name="add-pet"),
    path("<str:username>/pet/<slug:pet_slug>/", include([
        path("edit/", views.PetEditView.as_view(), name="edit-pet"),
        path("delete/", views.PetDeleteView.as_view(), name="delete-pet"),
        path("", views.PetDetailView.as_view(), name="pet-details"),
    ])),
]