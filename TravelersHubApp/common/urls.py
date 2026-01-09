from django.urls import path

from common.views import index, all_trips_view

urlpatterns = [
    path("", index, name="index"),
    path("all-trips/", all_trips_view, name="all-trips"),
]