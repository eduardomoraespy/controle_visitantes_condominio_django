from django.contrib import admin
from django.urls import path
from usuarios.views import home
from visitantes import views

urlpatterns = [
    path(
        'admin/',
        admin.site.urls
    ),

    path(
        '', 
        home, 
        name='home'
    ),

    path(
        'visitante/cadastro',
        views.registrar_visitante,
        name='registrar_visitante'
    ),

    path(
        'visitante/informacoes_visitante/<int:id>/',
        views.informacoes_visitante,
        name='informacoes_visitante'
    ),

    path(
        'visitante/finalizar-visita/<int:id>',
        views.finalizar_visita,
        name='finalizar_visita'
    )

]
