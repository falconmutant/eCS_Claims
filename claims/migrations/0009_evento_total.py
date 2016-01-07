# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0008_auto_20160107_0053'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='total',
            field=models.DecimalField(default=15155.1, max_digits=7, decimal_places=2),
            preserve_default=False,
        ),
    ]
