# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atendimentos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='estadoCivil',
            field=models.CharField(max_length=20, choices=[('solteiro(a)', 'Solteiro(a)'), ('casado(a)', 'Casado(a)'), ('divorciado(a)', 'Divorciado(a)'), ('viuvo', 'Viuvo(a)')], verbose_name='Estado Civil'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='queixaPrincipal',
            field=models.CharField(max_length=100, verbose_name='Queixa Principal'),
        ),
    ]
