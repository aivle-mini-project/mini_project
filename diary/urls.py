from django.urls import path
from . import views
app_name = 'diary'
urlpatterns = [
    path('create/',views.create, name = 'create'),
    path('detail/',views.detail, name = 'detail'),
    path('list/',views.list, name = 'list'),
    path('edit/',views.edit, name = 'edit'),
]