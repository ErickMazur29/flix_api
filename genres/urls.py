from django.urls import path
from . import views


urlpatterns = [
    path('genre/', views.GenreCreateListView.as_view(), name='genre_create_list'),
    path('genre/<int:pk>', views.GenreRetrieverUpdateDestroyView.as_view(), name='genre_retriever_update_destroy'),
]
