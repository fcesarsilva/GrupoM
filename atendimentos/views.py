from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.utils import timezone
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .form import PacienteForm
from .models import Paciente



def poslogin(request):

    if request.user.id:
     return render(request, 'Bem_vindo.html', {})
    else:
        return HttpResponseRedirect("/")


def cadastroPaciente(request):
     
     
 if not request.user.id: 
    return HttpResponseRedirect("/")
  
 else:    
    
    if request.method == 'POST':
              
        form = PacienteForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/inicio/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PacienteForm()

    return render(request, 'CadastroPaciente.html', {'form': form})
   


class PacienteListVeiw(ListView):

    model = Paciente
    def lista(self, **kwargs):
         
        list = super (PacienteListVeiw, self)
        return list        
        


class PacienteUpdate(UpdateView):
    model = Paciente
    success_url = '/inicio/lista/'
    fields = fields = ['nome','cpf','data_Nascimento','sexo','estadoCivil','data_Atendimento','queixaPrincipal',]   
   

class PacienteDelete(DeleteView):
    model = Paciente
    success_url = '/inicio/lista/'