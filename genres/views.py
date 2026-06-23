from rest_framework import generics
from genres.models import Genres
from genres.serializers import GenreSerializer

# CreateListView feita em CBV's
class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genres.objects.all() # mostrar todos da lista
    serializer_class = GenreSerializer

    
# RetrieverUpdateDeleteView feita em CBV's

class GenreRetrieverUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer