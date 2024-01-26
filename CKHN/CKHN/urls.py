"""
URL configuration for CKHN project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path ,re_path

from .views import *
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage_render,name=" '' " ),
    path('random/',randompage_render,name="random"),
    path('annuaire/',annuairepage_render,name="annuaire"),
    path('access/',accesspage_render,name="acces"),
    re_path(r'^bio/(?P<username>\w+)/$',biopage_render,name="bio"),#pour mettre des url personnalisé
    path("mdp/",mdppage_render, name= "mdp"),

    
]