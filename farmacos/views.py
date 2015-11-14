from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.utils import timezone
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Remedio
from .form import RemedioForm
# Create your views here.





class RemedioListVeiw(ListView):

    model = Remedio
    
    def get_queryset(self):

        remedio = Remedio.objects.all()
        q = self.request.GET.get('search_box')

        # Buscar por remedio
        if q is not None:
            remedio = Remedio.objects.filter(descricao_Medicamento__contains=q)
        return remedio
         
        list = super (RemedioListVeiw, self)
        return list 


def cadastroRemedio(request):
     
     
 if not request.user.id: 
    return HttpResponseRedirect("/")
  
 else:    
    
    if request.method == 'POST':
              
        form = RemedioForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/remedio/lista')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RemedioForm()

    return render(request, 'RemedioPaciente.html', {'form': form})


class RemedioUpdate(UpdateView):
    model = Remedio
    success_url = '/remedio/lista/'
    fields = fields = ['descricao_Medicamento',]


class RemedioDelete(DeleteView):
    model = Remedio
    success_url = '/remedio/lista/'    


class RemedioDetailView(DetailView):

    model = Remedio

    def Detalhes(self, **kwargs):
        detalhes = super(RemedioDetailView, self)
        
        return detalhes    