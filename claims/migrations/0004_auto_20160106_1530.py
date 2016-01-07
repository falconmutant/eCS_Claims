# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0003_cargos_sistemacodigo'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='hospital',
            field=models.CharField(default='Ejemplo', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proveedor',
            name='localidad',
            field=models.CharField(default='Ejemplo', max_length=255),
            preserve_default=False,
        ),
    ]
