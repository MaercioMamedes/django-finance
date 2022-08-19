from django.urls import path
from appUsers.views import register


urlpatterns = [
    path('register', register, name='register'),
]
