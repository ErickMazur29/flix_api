from rest_framework import generics
from reviews.models import Reviews
from reviews.serializers import ReviewSerializer

class ReviewCreateListView(generics.ListCreateAPIView):
    queryset= Reviews.objects.all()
    serializer_class = ReviewSerializer

class ReviewRetrieverUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
