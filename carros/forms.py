from django.forms import ModelForm
from .models import Montadora


class MontadoraForm(ModelForm):
    class Meta:
        model = Montadora
        fields = '__all__'

