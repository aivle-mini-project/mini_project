"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import showIndex
from EDuser.views import RegisterView, RegisterProfileView, toRegisterProfile, LoginView, logout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', showIndex, name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('toRegisterProfile/', toRegisterProfile, name= 'toRegisterProfile'),
    path('registerProfile/', RegisterProfileView, name= 'registerProfile'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('other/', include('otherpage.urls')),
    path('boardapi/',include('boardAPI.urls')),
    path('board/',include('board.urls')),
    path('diary/',include('diary.urls')),
    path('mypage/', include('mypage.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
