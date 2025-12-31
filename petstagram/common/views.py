from copy import copy
from urllib.request import Request

from django.contrib.admin.templatetags.admin_list import search_form
from django.http import HttpResponse
from django.shortcuts import render, redirect, resolve_url

from common.forms import CommentBaseForm, SearchForm
from common.models import Like
from photos.models import Photo


def home_page_view(request):
    all_photos = Photo.objects.prefetch_related("tagged_pets", "like_set").all()
    comment_form = CommentBaseForm(request.POST or None)
    searching_form = SearchForm(request.GET or None)

    if request.method == "GET" and searching_form.is_valid():
        all_photos = Photo.objects.filter(tagged_pets__name__icontains=searching_form.cleaned_data.get('text', ''))
    else:
        all_photos = Photo.objects.prefetch_related("tagged_pets", "like_set").all()


    context = {
        'all_photos': all_photos,
        'comment_form': comment_form,
        'search_form': searching_form,
    }
    return render(request, "common/home-page.html", context)


def like(request, photo_id: int):
    # photo = Photo.objects.get(pk=photo_id)
    like_object = Like.objects.filter(to_photo_id=photo_id).first()

    if like_object:
        like_object.delete()
    else:
        Like.objects.create(to_photo_id=photo_id)

    return redirect(request.META.get('HTTP_REFERER') + f"#{photo_id}")


def share(request, photo_id: int):
    copy(request.META.get('HTTP_HOST') + resolve_url("photo_details", photo_id))

    return redirect(request.META.get('HTTP_REFERER') + f"#{photo_id}")


def add_comment(request, photo_id: int):
    comment_form = CommentBaseForm(request.POST or None)

    if request.method == "POST" and comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.to_photo = Photo.objects.get(pk=photo_id)
        comment.save()
        return redirect(request.META.get('HTTP_REFERER') + f"#{photo_id}")


















