from django.urls import path, include

from cars import views
from cars.views import catalogue_view

urlpatterns = [
    path("catalogue/", catalogue_view, name="catalogue"),
    path("create/", views.CreateCarView.as_view(), name="car-create"),
    path("<int:car_id>/", include([
        path("details/", views.DetailsCarView.as_view(), name="car-details"),
        path("edit/", views.EditCarView.as_view(), name="car-edit"),
        path("delete/", views.DeleteCarView.as_view(), name="car-delete"),
    ])),
]