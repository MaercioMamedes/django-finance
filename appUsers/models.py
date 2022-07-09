import email
from hashlib import new
from django.db import models
from django.contrib.auth.models import  User



class UserApp(models.Model):
    user = models.OneToOneField(User, max_length=200, on_delete=models.CASCADE)
    full_name = models.CharField('Nome completo', max_length=200)
    cell = models.CharField('Celular', max_length=13, default='')
    

    def __str__(self) -> str:
        return self.full_name


def factor_user(data_user):

    new_user = User.objects.create_user(username=data_user['user_name'],
                                        password=data_user['password'],
                                        email=data_user['email'],
                                        )

    new_user_app = UserApp(user=new_user,
                           full_name=data_user['fullname'],
                           cell=data_user['cell'])

    new_user_app.save()
