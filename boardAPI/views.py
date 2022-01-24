from django.shortcuts import render
from diary.models import Diary
from .serializers import DiarySerializer
from rest_framework.pagination import PageNumberPegination
from rest_framework import generics
from rest_framework import mixins

# Create your views here.
class BoardPagination(PageNumberPegination):
    page_size = 10
    
class DiaryListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = DiarySerializer
    pagination_class = BoardPagination


    def get_queryset(self):
        return Diary.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)




