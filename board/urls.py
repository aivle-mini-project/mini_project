from django.urls import path
from .views import boardView

app_name = 'board'
urlpatterns = [
    path('', boardView, name='board'),
]
