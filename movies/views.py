from django.db.models import Count, Avg
from rest_framework import generics, views, status, response
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from movies.models import Movies
from movies.serializers import MovieSerializer
from reviews.models import Reviews


class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer


class MovieRetrieverUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer


class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movies.objects.all()

    def get(self, request):
        total_movies = self.queryset.count()  # contagem dos filmes
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))  # lista os valores nome do genero(foreign key) e conta quantos id's ele possui
        total_reviews = Reviews.objects.count()  # contagem de reviews
        avg_rate = Reviews.objects.aggregate(avg_rating=Avg('rating'))['avg_rating']  # função para calucular a media das reviews

        return response.Response(
            data={
                "Total Movies": total_movies,
                "Movies_by_genre": movies_by_genre,
                "Total Reviews": total_reviews,
                "Avarage rate": round(avg_rate, 1) if avg_rate else 0  # list comprehesion para validação de campo
            },
            status=status.HTTP_200_OK
        )
