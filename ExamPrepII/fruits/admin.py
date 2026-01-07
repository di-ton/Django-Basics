from django.contrib import admin

from fruits.models import Fruit


@admin.register(Fruit)
class FruitAdmin(admin.ModelAdmin):
    exclude = ('owner',)
