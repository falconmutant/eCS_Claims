# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices_Web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emisor',
            name='numExterior',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='receptor',
            name='numExterior',
            field=models.CharField(max_length=255),
        ),
    ]
