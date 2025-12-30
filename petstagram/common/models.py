from django.db import models

from photos.models import Photo


class Comment(models.Model):
    text = models.TextField(max_length=300)
    date_and_time_of_publication = models.DateField(auto_now_add=True)
    to_photo = models.ForeignKey(to=Photo, on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]


class Like(models.Model):
    to_photo = models.ForeignKey(to=Photo, on_delete=models.CASCADE)
