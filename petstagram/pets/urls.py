from django.urls import path, include
from pets import views

urlpatterns = [
    path("add/", views.pet_add_view, name="add-pet"),
    path("<str:username>/pet/<slug:pet_slug>/", include([
        path("edit/", views.pet_edit_view, name="edit-pet"),
        path("delete/", views.pet_delete_view, name="delete-pet"),
        path("", views.pet_detail_view, name="pet-details"),
    ])),
]