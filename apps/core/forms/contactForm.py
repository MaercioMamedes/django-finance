from django.forms import ModelForm
from apps.core.models import MessageContact


class ContactForm(ModelForm):
    class Meta:
        model = MessageContact
        fields = '__all__'

    def clean(self):
        return self.cleaned_data
