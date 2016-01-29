# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0020_auto_20160119_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='fichaEmp',
            field=models.CharField(max_length=10),
        ),
    ]
