import json
from django.http import JsonResponse
from genres.models import Genres
from django.shortcuts import get_object_or_404 # função do django de indentificação dos objetos
from django.views.decorators.csrf import csrf_exempt # token de proteção

@csrf_exempt
def genre_create_list_view (request):
    # listar itens
    if request.method == 'GET':
        genres = Genres.objects.all()
        data = [{'id':genre.id, 'name': genre.name} for genre in genres]
        return JsonResponse (data, safe= False)
    

    # criar itens
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8')) # ler o que foi escrito no body e decodificar em utf-8
        new_genre = Genres(name = data['name']) # new genre será o que foi escrito no data do body
        new_genre.save() # salva a aplicação
        return JsonResponse(
            {
                'id': new_genre.id,
                'name': new_genre.name
            }, status=201
        )
    
@csrf_exempt
def genre_detail_update_delete_view(request, pk):
    # primary key fixa que será usada por todos
    genre = get_object_or_404(Genres, pk=pk)

    # detalhe do objeto
    if request.method == 'GET':
        data = {'id': genre.id, 'name': genre.name}
        return JsonResponse(data)
    

    # fazer alterações no objeto
    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        genre.name = data['name']
        genre.save()
        return JsonResponse(
            {
                'id': genre.id,
                'name': genre.name
            }, status=201
        )
    

    # deletar objeto
    elif request.method == 'DELETE':
        genre.delete()
        return JsonResponse(
            {'mensagem': 'Objeto excluído com sucesso!'},
            status=200,
        )
    
# todos json loads são coisas escritas no body