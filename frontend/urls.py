from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('fanpage/', views.fanpage, name='fanpage'),
    path('chat/', views.chat, name='chat'),
]