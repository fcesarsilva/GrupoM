from django.shortcuts import render
from django.http import HttpResponseRedirect
from form import PacienteForm
from django.shortcuts import render_to_response

def poslogin(request):
	
    return render(request, 'Bem_vindo.html', {})



def cadastroPaciente(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
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