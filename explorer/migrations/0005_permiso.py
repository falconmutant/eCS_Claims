# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0004_querylog_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='permiso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usuario', models.IntegerField(null=True)),
                ('reporte', models.IntegerField(null=True)),
                ('fecha', models.DateField()),
            ],
        ),
    ]
