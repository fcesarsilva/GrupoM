# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.PositiveIntegerField()),
                ('cartao_SUS', models.IntegerField(serialize=False, primary_key=True)),
                ('data_Nascimento', models.DateField()),
                ('sexo', models.CharField(max_length=20, choices=[('masculino', 'Masculino'), ('feminino', 'Feminino')])),
                ('estadoCivil', models.CharField(max_length=20, verbose_name=b'Estado Civil', choices=[('solteiro(a)', 'Solteiro(a)'), ('casado(a)', 'Casado(a)'), ('divorciado(a)', 'Divorciado(a)'), ('viuvo', 'Viuvo(a)')])),
                ('data_Atendimento', models.DateField()),
                ('queixaPrincipal', models.CharField(max_length=100, verbose_name=b'Queixa Principal')),
            ],
        ),
    ]
