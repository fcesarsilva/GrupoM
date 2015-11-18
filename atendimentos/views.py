from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.utils import timezone
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from core.views import LoginRequiredMixin
from .form import PacienteForm
from .models import Paciente


@login_required(login_url='/')
def poslogin(request):

    if request.user.id:
     return render(request, 'Bem_vindo.html', {})
    else:
        return HttpResponseRedirect("/")


@login_required(login_url='/')
def cadastroPaciente(request):
 
    if not request.user.has_perm('atendimentos.add_paciente'):
            return HttpResponseRedirect("/")
     
          
    
    if request.method == 'POST':
              
        form = PacienteForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/inicio/lista')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PacienteForm()

    return render(request, 'CadastroPaciente.html', {'form': form})
   


class PacienteListVeiw(LoginRequiredMixin,ListView):

    model = Paciente
    
         
    def get_queryset(self):
        if not self.request.user.has_perm('atendimentos.change_paciente'):
            raise PermissionDenied
        paciente = Paciente.objects.all()
        q = self.request.GET.get('search_box')

        # Buscar por Paciente
        if q is not None:
            paciente = Paciente.objects.filter(nome__contains=q)
        return paciente

        list = super (PacienteListVeiw, self)
        return list        
        

class PacienteUpdate(LoginRequiredMixin,UpdateView):
    model = Paciente
    success_url = '/inicio/lista/'
    fields = fields = ['nome','cpf','data_Nascimento','sexo','estadoCivil','data_Atendimento','queixaPrincipal',]   
   
    

class PacienteDelete(LoginRequiredMixin,DeleteView):
    model = Paciente
    success_url = '/inicio/lista/'
    




class PacienteDetailView(LoginRequiredMixin,DetailView):

    model = Paciente

    def Detalhes(self, **kwargs):
        
            detalhes = super(PacienteDetailView, self)
        
            return detalhes


@login_required(login_url='/')
def search(request):

    if not request.user.has_perm('atendimentos'):
            return HttpResponseRedirect("/")
    else: 

        if request.method == "POST":
             search_text = request.POST['pesquisa']
        else:
            search_text = ''

            paciente = Paciente.objects.filter(nome__contains=search_text)   

        return render(request,'atendimentos/paciente_list.html',{'Paciente':paciente})


