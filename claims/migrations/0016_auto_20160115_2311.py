# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0015_auto_20160115_2220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('secuencia', models.PositiveSmallIntegerField()),
                ('fechaApli', models.DateTimeField()),
                ('codigo', models.CharField(max_length=255)),
                ('descripcion', models.CharField(max_length=255)),
                ('udm', models.CharField(max_length=255)),
                ('sistema', models.CharField(max_length=255)),
                ('sistemaCodigo', models.CharField(max_length=255)),
                ('cantidad', models.PositiveSmallIntegerField()),
                ('precio', models.DecimalField(max_digits=7, decimal_places=2)),
                ('subtotal', models.DecimalField(max_digits=7, decimal_places=2)),
                ('iva', models.DecimalField(max_digits=7, decimal_places=2)),
                ('descuento', models.DecimalField(max_digits=7, decimal_places=2)),
                ('total', models.DecimalField(max_digits=7, decimal_places=2)),
                ('evento', models.ForeignKey(to='claims.Evento')),
            ],
        ),
        migrations.RenameModel(
            old_name='Procedimientos',
            new_name='Procedimiento',
        ),
        migrations.RemoveField(
            model_name='cargos',
            name='evento',
        ),
        migrations.AlterField(
            model_name='cargosdx',
            name='cargo',
            field=models.ForeignKey(to='claims.Cargo'),
        ),
        migrations.DeleteModel(
            name='Cargos',
        ),
    ]
