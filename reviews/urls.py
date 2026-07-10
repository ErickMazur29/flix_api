from django.urls import path
from . import views


urlpatterns = [
    path('review/', views.ReviewCreateListView.as_view(), name='review_create_list'),
    path('review/<int:pk>', views.ReviewRetrieverUpdateDestroyView.as_view(), name='review_retriever_update_destroy'),
]
