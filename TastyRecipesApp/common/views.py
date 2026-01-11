from django.shortcuts import render

from common.utils import get_profile


def home_view(request):
    profile = get_profile()
    context = {'profile': profile}
    return render(request, "home-page.html", context)
