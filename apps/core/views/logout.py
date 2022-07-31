from django.contrib import auth, messages
from django.shortcuts import redirect


def logout(request):
    auth.logout(request)
    messages.info(request, 'Nenhum usuário logado')

    return redirect('core:index')

