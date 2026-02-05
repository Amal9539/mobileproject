"""mobileproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from mobileapp import views  





urlpatterns = [
    path('login_get/', views.login_get, name='login_get'),
    path('login_post/', views.login_post, name='login_post'),

    path('home_get/',views.home_get, name='home_get'),
    path('user_get/', views.user_get, name='user_get'),
    path('user_post/', views.user_post, name='user_post'),
    path('user_view/', views.user_view, name='user_view'),
    path('user_action/', views.user_action, name='user_action'),
]
