from tabnanny import verbose
from django.db import models

class Visitante(models.Model):

    nome_completo = models.CharField(
        verbose_name='Nome Comple',
        max_length=194
    )

    cpf = models.CharField(
        verbose_name='CPF',
        max_length=11
    )

    data_nascimento = models.DateField(
        verbose_name='Data de Nascimento',
        auto_now=False,
        auto_now_add=False
    )

    numero_casa = models.PositiveSmallIntegerField(
        verbose_name='Número da casa'
    )

    placa_veiculo = models.CharField(
        verbose_name='Placa do Veículo',
        max_length=7,
        blank=True,
        null=True
    )

    horario_chegada = models.DateTimeField(
        verbose_name='Horário de chegada na portária',
        auto_now_add=True,
    )

    horario_saida = models.DateTimeField(
        verbose_name='Horário da saída do condomínio',
        auto_now=False,
        blank=True,
        null=True
    )

    horario_autorizacao = models.DateTimeField(
        verbose_name='Horário de autorização de entrada',
        auto_now=False,
        blank=True,
        null=True
    )

    morador_resposavel = models.CharField(
        verbose_name='Nome do morador responsável por autorizar a entrada do visitante',
        max_length=194,
        blank=True
    )

    registrado_por = models.ForeignKey(
        'porteiros.Porteiro',
        verbose_name='Porteiro responsável pelo registro',
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = 'visitante'
        verbose_name_plural = 'visitantes'
        db_table = 'visitante'
    

    def __str__(self):
        return self.nome_completo