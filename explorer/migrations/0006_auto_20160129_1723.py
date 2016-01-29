# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0005_permiso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permiso',
            name='usuario',
            field=models.TextField(null=True, blank=True),
        ),
    ]
