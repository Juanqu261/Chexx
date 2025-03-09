# bot_app/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.play_chess, name='play_chess'),
    path('bot_move/', views.bot_move, name='bot_move'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
