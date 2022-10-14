from pydoc import render_doc
from django.shortcuts import render
from apps.appUsers.models import UserApp


def game_players(request):

    users = UserApp.objects.all()

    return render(request, 'core/gamePlayers.html', {'users' : users})
