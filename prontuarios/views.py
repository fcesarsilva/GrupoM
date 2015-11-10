from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.utils import timezone
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .form import ProntuarioForm
from .models import Prontuario


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

# Create your views here.
