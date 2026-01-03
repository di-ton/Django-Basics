from django.urls import path, include
from photos import views

urlpatterns = [
    path("add/", views.PhotoAddView.as_view(), name="photo_add"),
    path("<int:pk>/", include([
        path("edit/", views.PhotoEditView.as_view(), name="photo_edit"),
        path("", views.PhotoDetailView.as_view(), name="photo_details"),
        path("delete/", views.photo_delete_view, name="photo_delete"),
    ]))

]










