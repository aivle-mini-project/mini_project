from django.urls import path
from .views import DiaryListAPI, req_json

app_name = 'boardAPI'
urlpatterns = [
    path('', DiaryListAPI.as_view(), name='boardAPI'),
    path('expressionPost/', req_json)
]
