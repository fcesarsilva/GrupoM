# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prontuarios', '0002_auto_20151114_0226'),
    ]

    operations = [
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
