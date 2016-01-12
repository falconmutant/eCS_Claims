# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0012_auto_20160111_1854'),
        ('invoices_Web', '0002_auto_20160110_0658'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autorizacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Estatus', models.CharField(max_length=255, choices=[('R', 'Recibido'), ('A', 'Aceptado PEMEX'), ('X', 'Rechazado PEMEX'), ('Y', 'Aceptado MAC'), ('N', 'Rechazado MAC'), ('E', 'En Revision')])),
                ('FechaSolicitud', models.DateField()),
                ('Comentarios', models.CharField(max_length=255, null=True)),
                ('TipoAprobacion', models.CharField(max_length=255)),
                ('Sistema', models.CharField(max_length=255)),
                ('comprobante', models.ForeignKey(to='invoices_Web.Comprobante')),
            ],
        ),
        migrations.CreateModel(
            name='ComprobanteEvento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comprobante', models.ForeignKey(to='invoices_Web.Comprobante')),
                ('evento', models.ForeignKey(to='claims.Evento')),
            ],
        ),
    ]
