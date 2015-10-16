# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommonInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
                ('matricula', models.PositiveIntegerField()),
                ('data_Admissao', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Enfermeiro',
            fields=[
                ('commoninfo_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='funcionarios.CommonInfo')),
                ('coren', models.PositiveIntegerField()),
                ('especialidade', models.CharField(max_length=50)),
            ],
            bases=('funcionarios.commoninfo',),
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('commoninfo_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='funcionarios.CommonInfo')),
                ('CRM', models.PositiveIntegerField()),
                ('especialidade', models.CharField(max_length=50)),
            ],
            bases=('funcionarios.commoninfo',),
        ),
        migrations.CreateModel(
            name='Recepcionista',
            fields=[
                ('commoninfo_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='funcionarios.CommonInfo')),
                ('cpf', models.PositiveIntegerField(serialize=False, primary_key=True)),
            ],
            bases=('funcionarios.commoninfo',),
        ),
    ]
