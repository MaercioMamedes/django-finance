from django.shortcuts import render
from appUsers.forms import UserAppForms, UserForms


def index(request):


    return render(request, 'core/index.html')
