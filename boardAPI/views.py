from django.shortcuts import render
from diary.models import Diary
from .serializers import DiarySerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from rest_framework import mixins
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from diary.models import Expression,Diary
from EDuser.models import Eduser

# Create your views here.
class BoardPagination(PageNumberPagination):
    page_size = 3

class DiaryListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = DiarySerializer
    pagination_class = BoardPagination

    def get_queryset(self):
        return Diary.objects.all().order_by('-id')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

@csrf_exempt
def req_json(request):
    if request.method == 'POST':
        obj = request.body.decode("utf-8")
        data = json.loads(obj)
        Expression.objects.create(user=Eduser.objects.get(username=data['username']),diary=Diary.objects.get(pk=data['diary_id']))
    return JsonResponse(data)