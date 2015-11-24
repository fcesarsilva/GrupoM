from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.utils import timezone
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from core.views import LoginRequiredMixin
from .form import ProntuarioForm
from .models import Prontuario


@login_required
def cadastroProntuario(request):
     
     
 if not request.user.id: 
    return HttpResponseRedirect("/")
  
 else:    
    
    if request.method == 'POST':
              
        form = ProntuarioForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/prontuario/lista')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProntuarioForm()

    return render(request, 'cadastroProntuario.html', {'prontuario': form})



class ProntuarioListVeiw(LoginRequiredMixin,ListView):
 
    model = Prontuario
    
    def get_queryset(self):
        prontuario = Prontuario.objects.all()
        q = self.request.GET.get('search_box')

        # Buscar por Prontuario
        if q is not None:
            prontuario = Prontuario.objects.filter(paciente__nome__contains=q)
        return prontuario
         
        list = super (ProntuarioListVeiw, self)
        return list 

class ProntuarioUpdate(LoginRequiredMixin,UpdateView):
    model = Prontuario
    success_url = '/prontuario/lista/'
    fields = fields = ['data_Consulta','paciente','medico','remedio',]   
   

class ProntuarioDelete(LoginRequiredMixin,DeleteView):
    model = Prontuario
    success_url = '/prontuario/lista/'


class ProntuarioDetailView(LoginRequiredMixin,DetailView):

    model = Prontuario

    def Detalhes(self, **kwargs):
        detalhes = super(ProntuarioDetailView, self)
        
        return detalhes         





class PrintView(LoginRequiredMixin,DetailView):

    model = Prontuario
    template_name = "prontuarios/prontuario_print.html"
    def Print(self, **kwargs):
        detalhes = super(PrintView, self)
        
        return detalhes   



class HistoricoView(LoginRequiredMixin,DetailView):

    model = Prontuario
    template_name = "prontuarios/prontuario_historico.html"
    def Print(self, **kwargs):
        detalhes = super(PrintView, self)
        
        return detalhes         