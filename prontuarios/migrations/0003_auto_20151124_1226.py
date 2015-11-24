# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('atendimentos', '0002_auto_20151016_0951'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('prontuarios', '0002_auto_20151114_0226'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalProntuario',
            fields=[
                ('codigo_Prontuario', models.IntegerField(db_index=True, blank=True)),
                ('data_Consulta', models.DateField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, null=True, to=settings.AUTH_USER_MODEL)),
                ('paciente', models.ForeignKey(related_name='+', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, blank=True, null=True, to='atendimentos.Paciente')),
            ],
            options={
                'get_latest_by': 'history_date',
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical prontuario',
            },
        ),
        migrations.RemoveField(
            model_name='prontuario',
            name='id',
        ),
        migrations.AlterField(
            model_name='prontuario',
            name='codigo_Prontuario',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='prontuario',
            name='medico',
            field=models.ManyToManyField(to='funcionarios.Medico'),
        ),
        migrations.AlterField(
            model_name='prontuario',
            name='remedio',
            field=models.ManyToManyField(to='farmacos.Remedio'),
        ),
    ]
