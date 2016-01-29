# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0017_auto_20160115_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autorizacion',
            name='Estatus',
            field=models.CharField(max_length=255, choices=[('R', 'Recibido'), ('A', 'Aceptado PEMEX'), ('X', 'Rechazado PEMEX'), ('Y', 'Aceptado MAC'), ('N', 'Rechazado MAC'), ('E', 'En Revision MAC'), ('P', 'En Revision PEMEX')]),
        ),
        migrations.AlterField(
            model_name='dx',
            name='admision',
            field=models.CharField(default='N', max_length=1, choices=[('Y', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='dx',
            name='fecha',
            field=models.DateField(default='2016-01-16'),
        ),
        migrations.AlterField(
            model_name='tipousuario',
            name='tipo',
            field=models.CharField(max_length=1, choices=[('M', 'MAC'), ('P', 'PEMEX'), ('E', 'ECARESOFT')]),
        ),
    ]
