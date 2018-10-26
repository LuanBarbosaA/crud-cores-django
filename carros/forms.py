from django.forms import ModelForm
from .models import *
from django import forms
from django.forms import *


class MontadoraForm(ModelForm):
    class Meta:
        model = Montadora
        fields = '__all__'


class CorForm(ModelForm):
    #opcao = TextInput(attrs={'name': 'opcao', 'class': 'invisible'})
    class Meta:
        model = Cor
        fields = '__all__'

