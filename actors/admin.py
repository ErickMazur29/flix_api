from django.contrib import admin
from actors.models import Actors
# Register your models here.

@admin.register(Actors)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birthday', 'nationality','age')
    search_fields = ('name',),
