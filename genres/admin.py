from django.contrib import admin
from genres.models import Genres
# Register your models here.

@admin.register(Genres)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',),

