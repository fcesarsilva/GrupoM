# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prontuarios', '0003_auto_20151117_0418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prontuario',
            name='id',
        ),
        migrations.AlterField(
            model_name='prontuario',
            name='codigo_Prontuario',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
