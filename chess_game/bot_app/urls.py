# bot_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.play_chess, name='play_chess'),
    path('bot_move/', views.bot_move, name='bot_move'),
]
