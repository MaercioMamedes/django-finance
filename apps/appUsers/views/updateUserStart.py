from django.shortcuts import render
from appUsers.forms import UserForms


def update_user_start(request):
    user_form = UserForms()

    return render(request, 'appUsers/updateUser.html', {'user_form':user_form})
