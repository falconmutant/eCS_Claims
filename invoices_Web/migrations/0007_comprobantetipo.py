# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices_Web', '0006_auto_20160112_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComprobanteTipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=1, choices=[('1', '1er Nivel'), ('2', '2do Nivel'), ('3', '3er Nivel')])),
                ('fecha', models.DateField()),
                ('usuario', models.IntegerField()),
                ('comprobante', models.IntegerField()),
            ],
        ),
    ]
