from unicodedata import numeric
from django.contrib.auth.models import User

# TESTAR ESSES VALIDADORES

"""Verifica campos em branco"""


def check_empty(field, list_errors):
    print(field)
    if not field.strip():
        list_errors[field] = f'O campo {field} não pode está vazio'


"""Verifica se senha ou email são  válidos"""


def check_field_equal(field, field_confirm, list_errors):
    if field.strip() != field_confirm.strip():
        list_errors[field] = 'Senhas diferentes ou nulas'


def check_is_alpha_numeric(field, list_errors):
    if any(char.isdigit() for char in field):
        list_errors[field] = 'Nome completo não pode conter números'
