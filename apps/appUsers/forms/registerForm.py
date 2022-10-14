from django.forms import CharField, EmailField, ModelForm, PasswordInput, Form
from apps.appUsers.models import UserApp
from django.contrib.auth.models import User
from apps.appUsers.helpers import check_empty, check_field_equal


class UserForms(Form):
    fullname = CharField(label='Nome Completo', max_length=200)
    username = CharField(label='usuário de Login', max_length=100)
    email = EmailField(label='email', max_length=100)
    cell = CharField(label='Celular', max_length=11)
    password = CharField(label='senha', widget=PasswordInput())
    password_confirm = CharField(label='confirme sua senha', widget=PasswordInput())

    def clean(self):

        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        list_errors = {}

        check_empty(username, list_errors)
        check_empty(email, list_errors)
        check_field_equal(password, password_confirm, list_errors)

        if list_errors is not None:
            for error in list_errors:
                message_error = list_errors[error]
                self.add_error(error, message_error)

        return self.cleaned_data
