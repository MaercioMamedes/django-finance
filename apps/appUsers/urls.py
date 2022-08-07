from django.urls import path
from appUsers.views import register

app_name = 'appUsers'
urlpatterns = [
    path('register', register, name='register'),
]
