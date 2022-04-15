from django.db import models


class Porteiro(models.Model):

    # vincular models
    usuario = models.OneToOneField(
        'usuarios.Usuario',
        verbose_name='Usuário',
        on_delete=models.PROTECT #nunca será excluído
    ) # Relacão 1 para 1

    nome_completo = models.CharField(
        verbose_name='Nome completo',
        max_length=194,
    )

    cpf = models.CharField(
        verbose_name='CPF',
        max_length=11,
    )

    telefone = models.CharField(
        verbose_name='Telefone de Contato',
        max_length=11,
    )

    data_nascimento = models.DateField(
        verbose_name='Data de Nasciemento',
        auto_now=False, # nunca irá ser atualizado
        auto_now_add=False # não irá setar com a data atual
    )


    class Meta:
        verbose_name = 'porteiro'
        verbose_name_plural = 'porteiros'
        db_table = 'porteiro'

    def __str__(self):
        return self.nome_completo
