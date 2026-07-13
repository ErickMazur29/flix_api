from django.db.models import Avg, Count, Min, Max
from rest_framework import serializers
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer
from movies.models import Movies


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movies
        fields = "__all__"

    def validate_release_date(self, value):
        if value.year < 1980:
            raise serializers.ValidationError('Atenção! O Filme precisa ter uma data superior a 1980.')
        return value

    def validate_resume(self, value):
        if len(value) > 300:
            raise serializers.ValidationError('O Resumo precisa ter no máximo 200 caracteres')
        return value


# classe apenas para GET
class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    rating_avarage = serializers.SerializerMethodField(read_only=True)
    total_rating = serializers.SerializerMethodField(read_only=True)
    min_rating = serializers.SerializerMethodField(read_only=True)
    max_rating = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movies
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rating_avarage', 'total_rating', 'min_rating', 'max_rating', 'resume']

    # metodo: média das avaliações
    def get_rating_avarage(self, obj):

        avarage = obj.review_movie.aggregate(Avg('rating'))['rating__avg']
        if avarage:
            return round(avarage, 1)
        return None

    # metodo: quantidade de avaliações
    def get_total_rating(self, obj):
        total = obj.review_movie.aggregate(Count('rating'))['rating__count']
        if total:
            return total
        return None

    # metodo: menor avaliação
    def get_min_rating(self, obj):
        minimo = obj.review_movie.aggregate(Min('rating'))['rating__min']
        if minimo:
            return minimo

        return None

    # metodo: maior avaliação
    def get_max_rating(self, obj):
        maximo = obj.review_movie.aggregate(Max('rating'))['rating__max']
        if maximo:
            return maximo
        return None
