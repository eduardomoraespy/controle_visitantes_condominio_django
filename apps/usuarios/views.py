from django.shortcuts import render
from visitantes import models

# Create your views here.

def home(request):

    todos_visitantes = models.Visitante.objects.all().order_by('-id')
    
    context = {
        'nome_pagina': 'Inicío da Dashborad',
        'todos_visitantes':todos_visitantes
    }# Dicionário de contexto

    return render(request, 'index.html', context)
