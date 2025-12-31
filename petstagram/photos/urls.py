from django.urls import path, include
from photos import views

urlpatterns = [
    path("add/", views.photo_add_view, name="photo_add"),
    path("<int:pk>/", include([
        path("edit/", views.photo_edit_view, name="photo_edit"),
        path("", views.photo_details_view, name="photo_details"),
        path("delete/", views.photo_delete_view, name="photo_delete"),
    ]))

]










