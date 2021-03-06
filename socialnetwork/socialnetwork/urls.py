"""socialnetwork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
from apps.views import *


router = routers.DefaultRouter()

router.register(r'profiles', ProfileView, base_name='profiles')
router.register(r'posts', PostView, base_name='posts')
router.register(r'comments', CommentView, base_name='comments')


urlpatterns = [
    path('admin/', admin.site.urls),
    
]

urlpatterns = router.urls + urlpatterns