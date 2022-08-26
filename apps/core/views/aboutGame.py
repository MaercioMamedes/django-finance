from django.shortcuts import render


def about_game(request):
    return render(request, 'core/aboutGame.html')
    