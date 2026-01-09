from django.shortcuts import render

from common.utilis import get_profile
from trips.models import Trip


def index(request):
    traveler = get_profile()
    context = {'traveler': traveler}
    return render(request, 'index.html', context)


def all_trips_view(request):
    traveler = get_profile()
    trips = Trip.objects.filter(traveler=traveler).order_by("-start_date")
    context = {'traveler': traveler, "trips": trips}
    return render(request, "all-trips.html", context)