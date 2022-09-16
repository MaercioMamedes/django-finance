from django.db import models
from django.contrib.auth.models import  User
from django.core.exceptions import ValidationError


class Asset(models.Model):
    name = models.CharField('Nome da Empresa', max_length=200)
    ticker = models.CharField('código do papel', max_length=10)
    price = models.DecimalField('valor da cota', max_digits=7,decimal_places=2)
    url_image = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.name


class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    assets_wallet = models.ManyToManyField(Asset)

    def clean(self):
        if len(self.assets_wallet.all()) == 5:
            raise ValidationError('carteira já contém 5 elementos')
        
        else:
            return True
    
            