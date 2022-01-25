from django.urls import path
from . import views

app_name = 'otherpage'

urlpatterns = [
    path('show_date/', views.show_date, name='date'),
    path('show_week/', views.show_week, name='week'),
]
