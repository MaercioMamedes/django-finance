from django.db import models


class MessageContact(models.Model):
    fullname = models.CharField('Nome Completo', max_length=100)
    email = models.CharField('email', max_length=100)
    subject = models.CharField('Assunto', max_length=100)
    message_content = models.TextField('Menssagem')

    class Meta:
        app_label = 'apps.core'
