from rest_framework import serializers
from movies.models import Movies
from django.db.models import Avg

class MovieSerializer(serializers.ModelSerializer):
    rating_avarage = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movies
        fields = "__all__"

    def get_rating_avarage(self, obj):
        avarage = obj.review_movie.aggregate(Avg('rating'))['rating__avg']

        if avarage:
            return round(avarage, 1)
        
        return None

    def validate_release_date(self, value):
        if value.year < 1980:
            raise serializers.ValidationError('Atenção! O Filme precisa ter uma data superior a 1980.')
        return value
    
    def validate_resume(self, value):
        if len(value) > 300:
            raise serializers.ValidationError('O Resumo precisa ter no máximo 200 caracteres')
        return value