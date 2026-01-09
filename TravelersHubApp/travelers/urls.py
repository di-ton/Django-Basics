from django.urls import path

from travelers import views

urlpatterns = [
    path("create/", views.CreateTravelerView.as_view(), name="create-traveler"),
    path("<int:traveler_id>/details/", views.DetailsTravelerView.as_view(), name="details-traveler"),
    path("<int:traveler_id>/edit/", views.EditTravelerView.as_view(), name="edit-traveler"),
    path("<int:traveler_id>/delete/", views.DeleteTravelerView.as_view(), name="delete-traveler"),

]