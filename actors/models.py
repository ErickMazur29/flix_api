from django.db import models

class Actors(models.Model):
    NATIONALITY_CHOICES = [
        ("US", "Estados Unidos"),
        ("BR", "Brasil"),
    ]
    
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100, choices=NATIONALITY_CHOICES, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Actors"

    def __str__(self):
        return self.name