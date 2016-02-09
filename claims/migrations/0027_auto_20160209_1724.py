# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0026_auto_20160209_1719'),
    ]

    operations = [
        migrations.RenameField(
            model_name='motivos',
            old_name='is_active',
            new_name='active',
        ),
    ]
