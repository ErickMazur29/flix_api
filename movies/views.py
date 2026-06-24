from rest_framework import generics
from movies.models import Movies
from movies.serializers import MovieSerializer

class MovieCreateListView(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

class MovieRetrieverUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer