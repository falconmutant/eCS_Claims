# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0007_auto_20160106_1802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='total',
        ),
        migrations.AlterField(
            model_name='dx',
            name='estatus',
            field=models.CharField(max_length=1, choices=[('A', 'Activo'), ('I', 'Inactivo'), ('R', 'Resuelto')]),
        ),
    ]
