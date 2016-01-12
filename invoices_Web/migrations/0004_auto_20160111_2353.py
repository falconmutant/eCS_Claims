# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices_Web', '0003_autorizacion_comprobanteevento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprobanteevento',
            name='comprobante',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='comprobanteevento',
            name='evento',
            field=models.IntegerField(),
        ),
    ]
