# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('claims', '0018_auto_20160116_0022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipousuario',
            name='usuario_id',
        ),
        migrations.AddField(
            model_name='tipousuario',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dx',
            name='fecha',
            field=models.DateField(default='2016-01-19'),
        ),
    ]
