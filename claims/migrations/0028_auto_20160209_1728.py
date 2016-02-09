# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0027_auto_20160209_1724'),
    ]

    operations = [
        migrations.RenameField(
            model_name='motivos',
            old_name='active',
            new_name='is_active',
        ),
    ]
