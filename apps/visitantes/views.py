import re
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from visitantes.forms import CadastroVisitanteForm, AutorizaVisitanteForm
from visitantes.models import Visitante

from django.utils import timezone

from django.http import HttpResponseNotAllowed

#@login_required
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

#@login_required
def informacoes_visitante(request, id):

    visitante = get_object_or_404(Visitante, id=id)

    form = AutorizaVisitanteForm()

    if request.method == 'POST':
        form = AutorizaVisitanteForm(request.POST, instance=visitante)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.status = 'EM_VISITA'
            instance.horario_autorizacao = timezone.now()
            instance.save()

            messages.success(
                request, f'Entrada do(a) visitante {instance.nome_completo} autorizada pelo(a) morador(a){instance.morador_resposavel} com sucesso'
            )

            return redirect('home')

    context = {
        'nome_pagina': 'Informações visitante',
        'visitante' :visitante,
        'form' :form
    }

    return render(request, 'informacoes_visitante.html', context)

#@login_required
def finalizar_visita(request, id):

    if request.method == "POST":
        visitante = get_object_or_404(
            Visitante,
            id=id
        )

        visitante.status = 'FINALIZADO'
        visitante.horario_saida = timezone.now()

        visitante.save()

        messages.success(
            request,
            f'Visita do(a) {visitante.nome_completo} finalizado com sucesso'
        )

        return redirect('home')
    
    else:
        return HttpResponseNotAllowed(
            ['POST'],
            'Método não permitido'
        )