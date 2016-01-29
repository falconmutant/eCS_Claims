# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0014_auto_20160115_0044'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usuario_id', models.IntegerField()),
                ('tipo', models.CharField(max_length=1, choices=[('M', 'MAC'), ('P', 'PEMEX'), ('E', 'ECARESOFT'), ('S', 'SUPERADMIN')])),
            ],
        ),
        migrations.AlterField(
            model_name='dx',
            name='admision',
            field=models.CharField(default='N', max_length=1, choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='dx',
            name='fecha',
            field=models.DateField(default='2016-01-15'),
        ),
        migrations.AlterField(
            model_name='dx',
            name='medico',
            field=models.ForeignKey(to='claims.Medico', null=True),
        ),
    ]
