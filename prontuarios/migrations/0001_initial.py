# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmacos', '0001_initial'),
        ('funcionarios', '0001_initial'),
        ('atendimentos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prontuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo_Prontuario', models.IntegerField()),
                ('data_Consulta', models.DateField()),
                ('medico', models.ManyToManyField(to='funcionarios.Medico')),
                ('paciente', models.ForeignKey(to='atendimentos.Paciente')),
                ('remedio', models.ManyToManyField(to='farmacos.Remedio')),
            ],
        ),
    ]
