from urllib.request import Request

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect

from common.forms import CommentBaseForm
from pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from pets.models import Pet


def pet_add_view(request: HttpRequest) -> HttpResponse:
    form = PetCreateForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('profile-details', pk=1)

    context = {
        "form": form,
    }
    return render(request, "pets/pet-add-page.html", context)


def pet_detail_view(request: HttpRequest, username:str, pet_slug:str) -> HttpResponse:
    pet = Pet.objects.get(slug=pet_slug)
    comment_form = CommentBaseForm(request.POST or None)

    all_photos = pet.photo_set.prefetch_related("tagged_pets", "like_set").all()

    context = {
        "pet": pet,
        "all_photos": all_photos,
        "comment_form": comment_form,
    }
    return render(request, "pets/pet-details-page.html", context)

def pet_edit_view(request: HttpRequest, username:str, pet_slug:str) -> HttpResponse:
    pet = Pet.objects.get(slug=pet_slug)
    form = PetEditForm(request.POST or None, instance=pet)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('profile-details', pk=1)

    context = {
        "pet": pet,
        "form": form,
    }
    return render(request, "pets/pet-edit-page.html", context)


def pet_delete_view(request: HttpRequest, username:str, pet_slug:str) -> HttpResponse:
    pet=Pet.objects.get(slug=pet_slug)
    form = PetDeleteForm(instance=pet)

    if request.method == "POST":
        pet.delete()
        return redirect('profile-details', pk=1)

    context = {
        "pet": pet,
        "form": form,
    }

    return render(request, "pets/pet-delete-page.html", context)
















