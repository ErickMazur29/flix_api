from rest_framework import generics
from actors.models import Actors
from actors.serializers import ActorSerializer

class ActorCreateListView(generics.ListCreateAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieverUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorSerializer
