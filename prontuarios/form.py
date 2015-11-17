from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Prontuario

class ProntuarioForm(forms.ModelForm):

    class Meta:
        model = Prontuario
        fields = ('codigo_Prontuario','data_Consulta','paciente','medico','remedio',)
        



    class Media:
        css = {
            'all':['admin/css/widgets.css',
                   'css/uid-manage-form.css'],
        }
        # Adding this javascript is crucial
        js = ['/admin/jsi18n/']    