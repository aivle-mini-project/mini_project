from django.shortcuts import render
from diary.models import Diary
from .serializers import DiarySerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from rest_framework import mixins

# Create your views here.
class BoardPagination(PageNumberPagination):
    page_size = 3

class DiaryListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = DiarySerializer

    def get_queryset(self):
        return Diary.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
