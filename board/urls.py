from django.urls import path
from .views import boardView,boardTestView

app_name = 'board'
urlpatterns = [
    path('', boardView, name='board'),
    path('test', boardTestView, name='boardtest'),
]
