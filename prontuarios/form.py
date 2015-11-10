from django import forms
from .models import Prontuario

class ProntuarioForm(forms.ModelForm):

    class Meta:
        model = Prontuario
        fields = ('codigo_Prontuario','data_Consulta','paciente','medico','remedio',)