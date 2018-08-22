"""flick URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path

from .views import DownloadGroups, GetGroupPhotos, PhotoInfo, GetGroups, GetPhotos, Login, SignUp, GetPhotoInfo, UserSessionCalls, TopPhotos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('group', DownloadGroups.as_view()),
    path('groupphotos', GetGroupPhotos.as_view()),
    path('photoinfo', PhotoInfo.as_view()),
    path('getgroups', GetGroups.as_view()),
    path('getphotos', GetPhotos.as_view()),
    path('login/', Login.as_view()),
    path('signup/', SignUp.as_view()),
    path('getphotoinfo', GetPhotoInfo.as_view()),
    path('usercalls', UserSessionCalls.as_view()),
    path('topphotos', TopPhotos.as_view()),
]
