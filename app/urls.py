from django.contrib import admin
from django.urls import path
from django.http import JsonResponse

def test_view(request):
    return JsonResponse({'message':'Hello World'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', test_view, name='teste'),
]
