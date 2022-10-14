from django.urls import path
from apps.core.views import index, contact, login, logout, about_game, game_players


urlpatterns = [
    path('', index, name='index'),
    path('contato', contact, name='contact'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('game', about_game, name='about_game'),
    path('jogares', game_players, name='game_players'),
]
