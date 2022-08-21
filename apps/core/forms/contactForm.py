from django.forms import  ModelForm
from core.models import MessageContact


class ContactForm(ModelForm):
    class Meta:
        model = MessageContact
        fields = '__all__'


    def clean(self):
        
        return self.cleaned_data
