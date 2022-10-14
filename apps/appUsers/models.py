from django.db import models
from django.contrib.auth.models import User
from django.db.models import CharField


class UserApp(models.Model):
    user = models.OneToOneField(User, max_length=200, on_delete=models.CASCADE)
    full_name = models.CharField('Nome completo', max_length=200)
    cell = models.CharField('Celular', max_length=13, default='')

    def __str__(self) -> CharField:
        return self.full_name
