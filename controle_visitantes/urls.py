from re import template
from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views

from dashboard.views import home
from visitantes import views

urlpatterns = [
    path(
        'admin/',
        admin.site.urls
    ),

    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='login.html'
        ),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(
            template_name='logout.html'
        ),
        name='logout'
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
