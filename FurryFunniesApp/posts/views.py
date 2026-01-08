from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from authors.models import Author
from common.utilis import get_profile
from posts.forms import PostCreateForm, PostEditForm, PostDeleteForm
from posts.models import Post


class CreatePostView(CreateView):
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy("dashboard")
    template_name = "create-post.html"

    def form_valid(self, form):
        form.instance.author = Author.objects.first()
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "details-post.html"
    pk_url_kwarg = "post_id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["author"] = get_profile()
        return context


class EditPostView(UpdateView):
    model = Post
    form_class = PostEditForm
    success_url = reverse_lazy("dashboard")
    template_name = "edit-post.html"
    pk_url_kwarg = "post_id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["author"] = get_profile()
        return context



class DeletePostView(UpdateView):
    model = Post
    context_object_name = "post"
    template_name = "delete-post.html"
    pk_url_kwarg = "post_id"
    success_url = reverse_lazy("dashboard")
    form_class = PostDeleteForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["author"] = get_profile()
        return context

    def form_valid(self, form):
        self.object.delete()
        return redirect(self.success_url)

