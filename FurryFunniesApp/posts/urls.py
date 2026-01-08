from django.urls import path

from posts import views

urlpatterns = [
    path("", views.CreatePostView.as_view(), name="create-post"),
    path("<int:post_id>/details/", views.PostDetailView.as_view(), name="details-post"),
    path("<int:post_id>/edit/", views.EditPostView.as_view(), name="edit-post"),
    path("<int:post_id>/delete/", views.DeletePostView.as_view(), name="delete-post"),
]