# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices_Web', '0005_auto_20160112_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='comprobante',
            name='file_pdf',
            field=models.CharField(default='167856_10001326.pdf', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comprobante',
            name='file_xml',
            field=models.CharField(default='167856_10001326.xml', max_length=255),
            preserve_default=False,
        ),
    ]
