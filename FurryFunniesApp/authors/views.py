from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from authors.forms import AuthorForm, AuthorEditForm
from authors.models import Author


class AuthorCreateView(CreateView):
    model = Author
    template_name = "create-author.html"
    success_url = reverse_lazy("dashboard")
    form_class = AuthorForm


# class AuthorDetailView(DetailView):
#     model = Author
#     template_name = "details-author.html"
#     context_object_name = "author"
#     pk_url_kwarg = "author_id"

class AuthorDetailView(DetailView):
    model = Author
    template_name = "details-author.html"
    context_object_name = "author"

    def get_object(self):
        return Author.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["last_post"] = (
            self.object.post_set.order_by("-updated_at").first()
        )
        return context

class AuthorEditView(UpdateView):
    model = Author
    template_name = "edit-author.html"
    form_class = AuthorEditForm
    pk_url_kwarg = "author_id"
    context_object_name = "author"

    def get_success_url(self):
        return reverse_lazy("details-author", kwargs={"author_id": self.object.pk})


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = "delete-author.html"
    context_object_name = "author"
    success_url = reverse_lazy("index")
    pk_url_kwarg = "author_id"