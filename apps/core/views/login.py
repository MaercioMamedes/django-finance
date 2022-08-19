from django.contrib import auth, messages
from django.shortcuts import redirect, render
from core.forms import LoginForm



def login(request):
    if request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid():

            user_login = form.data.get('user_login')
            user_password = form.data.get('user_password')

            user_auth = auth.authenticate(request, username=user_login, password=user_password)

            if user_auth is not None:
                auth.login(request, user_auth)
                messages.success(request, 'Login realizado com sucesso')

                return redirect('core:index')
            
            else:
                messages.error(request, 'Login ou senhas inválidos')

                return redirect('core:login')

        else:

            messages.error(request, 'Login ou senha não podem está em branco')

            return redirect('core:login')

    
    else:

        login_form = LoginForm()

        return render(request, 'core/login.html', {'login_form' : login_form})

        