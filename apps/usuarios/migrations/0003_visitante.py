# Generated by Django 4.0.4 on 2022-04-15 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_alter_usuario_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=194, verbose_name='nome')),
            ],
            options={
                'db_table': 'visitante',
            },
        ),
    ]
