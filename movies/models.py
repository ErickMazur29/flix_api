from django.db import models
from genres.models import Genres
from actors.models import Actors

class Movies(models.Model):
    title = models.CharField(max_length=200)
    genre = models.ForeignKey(Genres, on_delete=models.PROTECT, related_name='genre_movies')
    release_date = models.DateField(null=True, blank=True)
    actors = models.ManyToManyField(Actors, related_name='actors_movies')
    resume = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Movies"

    def __str__(self):
        return self.title
