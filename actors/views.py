from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from actors.models import Actors
from actors.serializers import ActorSerializer

class ActorCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Actors.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieverUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Actors.objects.all()
    serializer_class = ActorSerializer
