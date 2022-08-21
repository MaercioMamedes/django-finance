import email
from django.db import models

# Create your models here.


class MessageContact(models.Model):
    fullname = models.CharField('Nome Completo', max_length=100)
    email = models.CharField('email',max_length=100)
    subject = models.CharField('Assunto', max_length=100)
    message_content = models.TextField('Menssagem')
