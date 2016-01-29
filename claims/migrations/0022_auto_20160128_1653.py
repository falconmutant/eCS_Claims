# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0021_auto_20160119_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dx',
            name='fecha',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='fichaEmp',
            field=models.CharField(max_length=12),
        ),
    ]
