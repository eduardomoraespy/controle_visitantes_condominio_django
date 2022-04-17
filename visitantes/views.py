from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from visitantes.forms import CadastroVisitanteForm
from visitantes.models import Visitante


def registrar_visitante(request):

    form = CadastroVisitanteForm()

    if request.method == "POST":
        form = CadastroVisitanteForm(request.POST)

        if form.is_valid():
            visitante = form.save(commit=False)
            
            visitante.registrado_por = request.user.porteiro
            visitante.save()

            messages.success(
                request, 
                f'Visitante {visitante.nome_completo} Registrado com Sucesso'
            )

            return redirect('home')
    
    context = {
        'nome_pagina':'Registrar visitantes',
        'form':form
    }

    return render(request, 'registrar_visitante/registrar_visitante.html', context)


def informacoes_visitante(request, id):

    visitante = get_object_or_404(Visitante, id=id)

    context = {
        'nome_pagina': 'Informações visitante',
        'visitante':visitante
    }

    return render(request, 'informacoes_visitante.html', context)
