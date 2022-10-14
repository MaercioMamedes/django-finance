from django.shortcuts import render, get_object_or_404, redirect
from apps.appUsers.models import UserApp
from django.contrib.auth.models import User


def update_user_start(request):
    user = get_object_or_404(User, pk=request.user.pk)

    user_app = get_object_or_404(UserApp, user=user)

    return render(request, 'appUsers/updateUser.html', {'user': user, 'user_app': user_app})


def update_user_end(request):
    if request.method == 'POST':
        user = get_object_or_404(User, pk=request.user.pk)

        user_app = get_object_or_404(UserApp, user=user)

        user_app.full_name = request.POST['fullname']
        user_app.cell = request.POST['cell']
        user_app.save()

        user.email = request.POST['email']
        user.save()

        return redirect('core:index')

    # return render(request, 'appUsers/updateUser.html', {'user': user, 'user_app': user_app})
