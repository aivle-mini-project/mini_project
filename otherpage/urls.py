from django.urls import path
from . import views

app_name = 'otherpage'

urlpatterns = [
    path('show/', views.load_statistics, name='statics'),
]
