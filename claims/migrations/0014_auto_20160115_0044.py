# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0013_auto_20160112_1818'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('secuencia', models.PositiveSmallIntegerField()),
                ('tipo', models.CharField(max_length=2, choices=[('PC', 'Familiar'), ('RP', 'Referencia'), ('AP', 'Admision'), ('TP', 'Atencion'), ('CP', 'Consultor'), ('CO', 'Cobertura'), ('AS', 'Asistente'), ('AN', 'Anesteciologo'), ('IN', 'Interprete'), ('ER', 'Urgenciologo'), ('PP', 'Cirujano')])),
                ('nombre', models.CharField(max_length=255)),
                ('especialidad', models.CharField(max_length=255)),
                ('cedula', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Procedimientos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('secuencia', models.PositiveSmallIntegerField()),
                ('sistema', models.CharField(max_length=255)),
                ('codigo', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=255)),
                ('fecha', models.DateField()),
                ('observaciones', models.CharField(max_length=255, null=True)),
                ('evento', models.ForeignKey(to='claims.Evento')),
                ('medico', models.ForeignKey(to='claims.Medico')),
            ],
        ),
        migrations.AddField(
            model_name='dx',
            name='admision',
            field=models.CharField(default='S', max_length=1, choices=[('S', 'Si'), ('N', 'No')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dx',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2016, 1, 15, 0, 44, 34, 806081, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dx',
            name='observaciones',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='dx',
            name='medico',
            field=models.ForeignKey(default=1, to='claims.Medico'),
            preserve_default=False,
        ),
    ]
