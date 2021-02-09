from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('',views.home, name='index'),
    path('chatroom/', views.chatroom, name='chatroom'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
  
]