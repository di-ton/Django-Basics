
from django.urls import path, include

from profiles import views

urlpatterns = [
    path('create/', views.CreateProfileView.as_view(), name='create-profile'),
    path('<int:pk>/details/', views.DetailProfileView.as_view(), name='details-profile'),
    path("<int:pk>/edit/", views.EditProfileView.as_view(), name='edit-profile'),
    path("<int:pk>/delete/", views.DeleteProfileView.as_view(), name='delete-profile'),
]