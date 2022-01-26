from django.urls import path
from . import views

app_name = 'calpage'

urlpatterns = [
    path('calpage/', views.Cal, name='calendar'),
]
