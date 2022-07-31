from django.contrib import auth, messages
from django.shortcuts import redirect, render



def login(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        user_password = request.POST['password']

        user_auth = auth.authenticate(request, username=user_name, password=user_password)

        if user_auth is not None:
            auth.login(request, user_auth)
            messages.success(request, 'Login realizado com sucesso')

            return redirect('core:index')
        
        else:
            messages.error(request, 'Login ou senhas inválidos')

            return redirect('core:login')
    
    return render(request, 'core/login.html')
        