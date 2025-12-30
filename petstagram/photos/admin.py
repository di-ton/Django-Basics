from django.contrib import admin


from photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'get_tagged_pets', 'date_of_publication']


    @staticmethod
    def get_tagged_pets(obj: Photo):
        return ", ".join(p.name for p in obj.tagged_pets.all())
