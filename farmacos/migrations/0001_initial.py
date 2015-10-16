from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Remedio',
            fields=[
                ('id_Medicamento', models.AutoField(serialize=False, primary_key=True)),
                ('descricao_Medicamento', models.CharField(max_length=30)),
            ],
        ),
    ]
