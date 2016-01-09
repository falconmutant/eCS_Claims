# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0010_auto_20160108_1949'),
    ]

    operations = [
        migrations.CreateModel(
            name='Motivos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('motivo', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='autorizacion',
            name='Estatus',
            field=models.CharField(max_length=255, choices=[('R', 'Recibido'), ('A', 'Aceptado'), ('X', 'Rechazado'), ('E', 'En Revision')]),
        ),
        migrations.AddField(
            model_name='autorizacion',
            name='motivo',
            field=models.ForeignKey(blank=True, to='claims.Motivos', null=True),
        ),
    ]
