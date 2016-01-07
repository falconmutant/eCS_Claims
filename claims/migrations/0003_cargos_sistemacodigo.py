# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0002_auto_20160105_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='cargos',
            name='sistemaCodigo',
            field=models.CharField(default='N/A', max_length=255),
            preserve_default=False,
        ),
    ]
