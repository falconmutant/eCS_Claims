# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CargosDx',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RenameField(
            model_name='cargos',
            old_name='sistemaCodificacion',
            new_name='sistema',
        ),
        migrations.RenameField(
            model_name='dx',
            old_name='dxvalue',
            new_name='codigo',
        ),
        migrations.RemoveField(
            model_name='cargos',
            name='dx',
        ),
        migrations.AddField(
            model_name='dx',
            name='nombre',
            field=models.CharField(default='Code', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cargosdx',
            name='cargo',
            field=models.ForeignKey(to='claims.Cargos'),
        ),
        migrations.AddField(
            model_name='cargosdx',
            name='dx',
            field=models.ForeignKey(to='claims.Dx'),
        ),
    ]
