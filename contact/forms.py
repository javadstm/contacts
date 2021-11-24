from django.forms import ModelForm
from .models import *



class ContactForm(ModelForm):
    class Meta:
        model = contact
        fields = '__all__'


