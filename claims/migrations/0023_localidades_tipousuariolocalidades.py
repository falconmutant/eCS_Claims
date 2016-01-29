# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('claims', '0022_auto_20160128_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='Localidades',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TipoUsuarioLocalidades',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('localidades', models.ForeignKey(to='claims.Localidades')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
