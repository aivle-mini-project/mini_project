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

from boardAPI.views import DiaryListAPI

from .views import showIndex
from EDuser.views import RegisterView, RegisterProfileView, toRegisterProfile, LoginView, logout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', showIndex, name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('toRegisterProfile/', toRegisterProfile),
    path('registerProfile/', RegisterProfileView),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('api/diary', DiaryListAPI.as_view()),
    path('other/', include('otherpage.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
