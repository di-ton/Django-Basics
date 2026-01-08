from django.urls import path

from common.views import index_view, dashboard_view

urlpatterns = [
    path("", index_view, name="index"),
    path("dashboard", dashboard_view, name="dashboard"),
]