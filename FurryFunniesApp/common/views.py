from django.shortcuts import render

from common.utilis import get_profile
from posts.models import Post


def index_view(request):
    author = get_profile()
    context = {'author': author}
    return render(request, "index.html")


def dashboard_view(request):
    author = get_profile()
    posts = Post.objects.filter(author=author)
    context = {'author': author, "posts": posts}
    return render(request, "dashboard.html", context)
