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