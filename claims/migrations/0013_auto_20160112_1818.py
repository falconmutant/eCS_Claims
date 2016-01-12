# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices_Web', '0005_auto_20160112_1818'),
        ('claims', '0012_auto_20160111_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='autorizacion',
            name='comprobante',
            field=models.ForeignKey(to='invoices_Web.Comprobante', null=True),
        ),
        migrations.AlterField(
            model_name='autorizacion',
            name='evento',
            field=models.ForeignKey(to='claims.Evento', null=True),
        ),
    ]
