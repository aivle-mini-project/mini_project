from django.urls import path
from . import views

app_name = 'diary_result'
urlpatterns = [
    path('',views.index, name = 'diary_result'),
    path('tagboard/<str:tag>/', views.tagBoard)
]
