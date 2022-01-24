from django.urls import path
from .views import DiaryListAPI

app_name = 'boardAPI'
urlpatterns = [
    path('', DiaryListAPI.as_view(), name='boardAPI'),
]
