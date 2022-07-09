from django.shortcuts import render
from .models import UserApp, factor_user
from django.contrib import messages
from . import helpers



def register(request):
    data_user = {}
    if request.method == 'POST':

        ### Data clean

        data_user = dict(request.POST)
        data_user.pop('csrfmiddlewaretoken')

        for element in data_user:

            data_user[element] = data_user[element][0]

            if helpers.check_empty(data_user[element][0]):

                messages.error(request, f'O {element} não pode está vazio')
                
                return render(request, 'appUsers/registerUser.html')                

        if not (helpers.check_field_equal(data_user['email'], data_user['email_confirm'])):

            messages.error(request, 'Os campos de emails estão divergente')
                
            return render(request, 'appUsers/registerUser.html') 


        if not (helpers.check_field_equal(data_user['password'], data_user['password_confirm'])):

            messages.error(request, 'Os campos de senhas estão divergente')
                
            return render(request, 'appUsers/registerUser.html') 


        #end Data clean
        
        """Create user"""
        factor_user(data_user)
        messages.success(request, 'cadastro realizado com sucesso realizado com sucesso')

        return render(request,'core/index.html')

    

    return render(request, 'appUsers/registerUser.html')

    