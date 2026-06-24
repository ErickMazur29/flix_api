from django.db import models
from movies.models import Movies
from django.core.validators import MinValueValidator, MaxValueValidator

class Reviews(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.PROTECT, related_name='review_movie')
    rating = models.PositiveIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5, 'A avaliação limite é de 5 estrelas!')
        ]
    )
    comment = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Reviews"

    def __str__(self):
        return self.movie
