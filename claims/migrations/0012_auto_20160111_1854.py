# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0011_auto_20160108_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autorizacion',
            name='Estatus',
            field=models.CharField(max_length=255, choices=[('R', 'Recibido'), ('A', 'Aceptado PEMEX'), ('X', 'Rechazado PEMEX'), ('Y', 'Aceptado MAC'), ('N', 'Rechazado MAC'), ('E', 'En Revision')]),
        ),
    ]
