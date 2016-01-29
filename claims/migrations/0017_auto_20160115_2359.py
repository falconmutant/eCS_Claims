# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0016_auto_20160115_2311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evento',
            old_name='medico',
            new_name='nommedico',
        ),
        migrations.AddField(
            model_name='medico',
            name='evento',
            field=models.ForeignKey(default=1, to='claims.Evento'),
            preserve_default=False,
        ),
    ]
