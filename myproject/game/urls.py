# game/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.play_game, name='play_game'),
]
