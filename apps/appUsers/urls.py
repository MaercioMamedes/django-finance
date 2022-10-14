from django.urls import path
from apps.appUsers.views import register, update_user_start, update_user_end


urlpatterns = [
    path('register', register, name='register'),
    path('update', update_user_start, name='update_user_start'),
    path('update-finish', update_user_end, name='update_user_end'),
]
