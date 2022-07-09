from django.contrib.auth.models import  User


"""Verifica campos em branco"""

def check_empty(field):
    return True if not field.strip() else False



"""Verifica se senha ou email são  válidos"""

def check_field_equal(field, field_confirm):
    return field == field_confirm
