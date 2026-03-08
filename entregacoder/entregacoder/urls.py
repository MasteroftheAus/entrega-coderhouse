"""
URL configuration for entregacoder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from miiapp import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name= "indexx"),
    path('home', views.home, name= "homme"),
    path('users_list/', views.users_list, name="lista"),
    path('user_detail/', views.users_detail, name='user_detail'),
]
