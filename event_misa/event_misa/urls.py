"""event_misa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from quickstart.api.api_views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('getBannerList/', bannerSlideList.as_view()),
    path('getEventByID/<int:id>/', getEventByID.as_view()), 
    path('getSpeakerList/', getSpeakerList.as_view()),
    path('getSpeakerByID/<uuid:id>/', getSpeakerByID.as_view()),
    path('getUserByEventID/<int:id>/', getUserByEventID.as_view()),
    path('deleteBannerSlideByID/<int:id>/', deleteBannerSlideByID.as_view()),
    path('deleteEventByID/<int:id>/', deleteEventByID.as_view()),
    path('deleteSpeakerByID/<uuid:id>/', deleteSpeakerByID.as_view()),
    path('InsertBannerSlide/', InsertBannerSlide.as_view()),
    path('InsertEvent/', InsertEvent.as_view()),
    path('GetAllEvent/',getAllEvent.as_view()),
]
