from django.urls import path

from authors import views

urlpatterns = [
    path("", views.AuthorCreateView.as_view(), name="create-author"),
    path("<int:author_id>/details/", views.AuthorDetailView.as_view(), name="details-author"),
    path("<int:author_id>/edit/", views.AuthorEditView.as_view(), name="edit-author"),
    path("<int:author_id>/delete/", views.AuthorDeleteView.as_view(), name="delete-author"),
]

