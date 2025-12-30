from urllib.request import Request

from django.http import HttpResponse
from django.shortcuts import render


def home_page_view(request):
    return render(request, "common/home-page.html")
