from django.shortcuts import render
from django.views.generic import TemplateView

from fruits.models import Fruit


def home_view(request):
    return render(request, "index.html")

class DashboardView(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fruits'] = Fruit.objects.all()
        return context