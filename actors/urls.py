from django.urls import path
from . import views


urlpatterns = [
    path('actor/', views.ActorCreateListView.as_view(), name='actor_create_list'),
    path('actor/<int:pk>', views.ActorRetrieverUpdateDestroyView.as_view(), name='actor_retriever_update_destroy'),
]
