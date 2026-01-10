from django.urls import path

from profiles import views

urlpatterns = [
    path('create/', views.CreateProfileView.as_view(), name='profile-create'),
    path("<int:pk>/details/", views.DetailsProfileView.as_view(), name='profile-details'),
    path("<int:pk>/edit/", views.EditProfileView.as_view(), name='profile-edit'),
    path("<int:pk>/delete/", views.DeleteProfileView.as_view(), name='profile-delete'),


]