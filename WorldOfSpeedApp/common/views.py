from django.shortcuts import render

from common.utils import get_profile


def index(request):
    profile = get_profile()
    context = {'profile': profile}
    return render(request, 'index.html', context)
