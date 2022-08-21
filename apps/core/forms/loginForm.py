from django.forms import Form, CharField, PasswordInput

class LoginForm(Form):
    user_login = CharField(label='Usuário')
    user_password = CharField(label='Senha', widget=PasswordInput())


    def clean(self):

        user_login = self.cleaned_data.get('user_login')
        user_password = self.cleaned_data.get('user_password')

        if (not user_login.strip()) or (not user_password.strip()):
            self.add_error('campo vazio','Login e senha não podem ser vazio')
        
        return self.cleaned_data
        