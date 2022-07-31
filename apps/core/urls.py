from django.urls import path
from core.views import *


app_name = 'core'
urlpatterns = [
    path('', index, name='index'),
    path('contato', contact, name='contact'),
    path('login', login, name='login'),
    path('logout', logout, name='logout')
]
