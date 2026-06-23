from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListView, GenreRetrieverUpdateDestroyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('genre/', GenreCreateListView.as_view(), name='genre_create_list'),
    path('genre/<int:pk>', GenreRetrieverUpdateDestroyView.as_view(), name='genre_detail'),
]
