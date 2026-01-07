from django.urls import path

from fruits import views

urlpatterns = [
    path('', views.CreateFruitView.as_view(), name='create-fruit'),
    path('<int:pk>/details/', views.DetailsFruitView.as_view(), name='details-fruit'),
    path('<int:pk>/edit/', views.EditFruitView.as_view(), name='edit-fruit'),
    path('<int:pk>/delete/', views.DeleteFruitView.as_view(), name='delete-fruit'),


]