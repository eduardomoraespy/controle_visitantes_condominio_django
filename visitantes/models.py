from tabnanny import verbose
from django.db import models

class Visitante(models.Model):

    STATUS_VISITANTE = [
        ('AGUARDANDO', 'Aguardando autorização'),
        ('EM_VISITA', 'Em Visita'),
        ('FINALIZADO', 'Visita Fianlizada'),
    ]

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

    status = models.CharField(
        verbose_name='Status',
        max_length=10,
        choices=STATUS_VISITANTE,
        default='AGUARDANDO'
    )

    # tratando campo vazio ou null
    def get_horario_saida(self):
        if self.horario_saida:
            return self.horario_saida
        
        return 'Horário de saída não registrado'

    def get_horario_autorizacao(self):
        if self.horario_autorizacao:
            return self.horario_autorizacao
        
        return 'Visitante aguardando autorização'
    
    def get_morador_resposavel(self):
        if self.morador_resposavel:
            return self.morador_resposavel
        
        return 'Visitante aguardando autorização'
    
    def get_placa_veiculo(self):
        if self.placa_veiculo:
            return self.placa_veiculo
        
        return 'Veículo não registrado'



    class Meta:
        verbose_name = 'visitante'
        verbose_name_plural = 'visitantes'
        db_table = 'visitante'
    

    def __str__(self):
        return self.nome_completo