from dataclasses import fields
from django import forms
from visitantes.models import Visitante


class CadastroVisitanteForm(forms.ModelForm):



    class Meta:
        model = Visitante
        fields = [
            'nome_completo', 'cpf', 'data_nascimento',
            'numero_casa', 'placa_veiculo', 
        ]
        error_messages = {
            'nome_completo':{
                'required':'O nome completo do visitante é obrigatório para o registro'
            },
            'cpf':{
                'required':'O CPF do visitante é obrigatório para o registro'
            },
            'data_nascimento':{
                'required':'A Data de Nascimento do visitante é obrigatória para o registro',
                'invalid':'Informe uma Data válida para a Data de Nascimento (DD/MM/AAAA)'
            },
            'numero_casa':{
                'required':'Por favor informe o Número da casa a ser visitada'
            },
        }


class AutorizaVisitanteForm(forms.ModelForm):

    morador_resposavel = forms.CharField(required=True)

    class Meta:
        model = Visitante
        fields = [
            'morador_resposavel'
        ]
        error_messages = {
            'morador_resposavel':{
                'required':'Por favor, informe o nome do morador responsavel por autorizar a entrada do visitante'
            },
        }