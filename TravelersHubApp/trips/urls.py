from django.urls import path

from trips import views

urlpatterns = [
    path("create/", views.TripCreateView.as_view(), name="create-trip"),
    path("<int:trip_id>/details/", views.TripDetailsView.as_view(), name="details-trip"),
    path("<int:trip_id>/edit/", views.TripEditView.as_view(), name="edit-trip"),
    path("<int:trip_id>/delete/", views.TripDeleteView.as_view(), name="delete-trip"),
]