from django.shortcuts import redirect, render,HttpResponse
from django.contrib import messages
from appUsers.forms import  UserForms
from django.contrib.auth.models import  User
from appUsers.models import UserApp



def register(request):

    if request.method == 'POST':
        form = UserForms(request.POST)
 
        if form.is_valid():
            
            new_user = User.objects.create_user(username=form.data.get('username'),
                                        password=form.data.get('password'),
                                        email=form.data.get('email'),
                                        first_name=form.data.get('fullname').split()[0],
                                        last_name=form.data.get('fullname').split()[-1],
                                        )

            new_user_app = UserApp.objects.create(user=new_user,
                           full_name=form.data.get('fullname'),
                           cell=form.data.get('cell'),
            )


        return redirect('core:login')


    formUser = UserForms()

    return render(request, 'appUsers/registerUser.html', {'formUser':formUser})

    