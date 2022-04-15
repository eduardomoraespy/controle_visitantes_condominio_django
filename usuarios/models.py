from django.db import models
# classes para criação de modelo personalizado de usuário
from django.contrib.auth.models import(
    BaseUserManager,
    AbstractBaseUser, 
    PermissionsMixin
)

class Usuario(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        verbose_name='Email',
        max_length=194,
        unique=True
    )

    # campos para modelo personalizado de usuários
    is_active = models.BooleanField(
        verbose_name='Usuário está ativo',
        default=True
    )

    is_staff = models.BooleanField(
        verbose_name='Usuário é da equipe de desenvolvimento',
        default=False
    )

    is_superuser = models.BooleanField(
        verbose_name='Usuário é um Super Usuário',
        default=False
    )

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'
        db_table = 'usuario'

    def __str__(self):
        return self.email