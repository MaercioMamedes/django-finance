from django.urls import path
from appUsers.views import register, update_user_start


urlpatterns = [
    path('register', register, name='register'),
    path('update', update_user_start, name='update_user_start'),
]
