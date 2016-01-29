# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0019_auto_20160119_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipousuario',
            name='tipo',
            field=models.CharField(max_length=1, choices=[('M', 'MAC'), ('P', 'PEMEX'), ('E', 'ECARESOFT'), ('S', 'SUPER USER')]),
        ),
    ]
