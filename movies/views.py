from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from movies.models import Movies
from movies.serializers import MovieSerializer

class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

class MovieRetrieverUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer