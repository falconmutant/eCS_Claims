# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app', models.CharField(default=b'App', max_length=50)),
                ('secret_key', models.CharField(max_length=64)),
                ('admins', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('credenciales', models.OneToOneField(related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
