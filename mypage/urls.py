from django.urls import path
from . import views


urlpatterns = [
    path('mypage/', views.mypage),
    path('mydiary/', views.mydiary),
    path('likepage/', views.likepage),
]

