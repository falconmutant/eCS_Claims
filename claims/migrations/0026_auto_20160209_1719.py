# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0025_auto_20160209_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motivos',
            name='is_active',
            field=models.CharField(max_length=1, choices=[('Y', 'Si'), ('N', 'No')]),
        ),
    ]
