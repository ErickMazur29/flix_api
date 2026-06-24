from django.urls import path
from . import views


urlpatterns = [
    path('movie/', views.MovieCreateListView.as_view(), name='movie_create_list'),
    path('movie/<int:pk>', views.MovieRetrieverUpdateDestroyView.as_view(), name='movie_retriever_update_destroy'),
]
