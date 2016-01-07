# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0006_auto_20160106_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autorizacion',
            name='Comentarios',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
