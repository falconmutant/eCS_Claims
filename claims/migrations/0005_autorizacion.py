# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0004_auto_20160106_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autorizacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Folio', models.CharField(max_length=255)),
                ('Estatus', models.CharField(max_length=255)),
                ('FechaSolicitud', models.DateField()),
                ('Comentarios', models.CharField(max_length=255)),
                ('TipoAprobacion', models.CharField(max_length=255)),
                ('Sistema', models.CharField(max_length=255)),
                ('evento', models.ForeignKey(to='claims.Evento')),
            ],
        ),
    ]
