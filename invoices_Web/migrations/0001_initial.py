# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comprobante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.CharField(max_length=5)),
                ('serie', models.CharField(max_length=2)),
                ('folio', models.CharField(max_length=255)),
                ('fecha', models.DateTimeField()),
                ('sello', models.TextField()),
                ('formaPago', models.CharField(max_length=255)),
                ('numCertificado', models.CharField(max_length=255)),
                ('certificado', models.TextField()),
                ('subtotal', models.DecimalField(max_digits=10, decimal_places=2)),
                ('tipocambio', models.CharField(max_length=2)),
                ('moneda', models.CharField(max_length=3)),
                ('total', models.DecimalField(max_digits=10, decimal_places=2)),
                ('tipocomprobante', models.CharField(max_length=255)),
                ('metodopago', models.CharField(max_length=255)),
                ('lugarexpedicion', models.CharField(max_length=255)),
                ('numCtaPago', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Conceptos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField()),
                ('unidad', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=255)),
                ('valorUnitario', models.DecimalField(max_digits=10, decimal_places=2)),
                ('importe', models.DecimalField(max_digits=10, decimal_places=2)),
                ('comprobante', models.ForeignKey(to='invoices_Web.Comprobante')),
            ],
        ),
        migrations.CreateModel(
            name='Emisor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rfc', models.CharField(max_length=13)),
                ('nombre', models.CharField(max_length=255)),
                ('calle', models.CharField(max_length=255)),
                ('numExterior', models.IntegerField()),
                ('colonia', models.CharField(max_length=255)),
                ('municipio', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=255)),
                ('pais', models.CharField(max_length=255)),
                ('codigoPostal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Impuesto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('impuesto', models.CharField(max_length=10)),
                ('tasa', models.IntegerField()),
                ('importe', models.DecimalField(max_digits=10, decimal_places=2)),
                ('comprobante', models.ForeignKey(to='invoices_Web.Comprobante')),
            ],
        ),
        migrations.CreateModel(
            name='Receptor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rfc', models.CharField(max_length=13)),
                ('nombre', models.CharField(max_length=255)),
                ('calle', models.CharField(max_length=255)),
                ('numExterior', models.IntegerField()),
                ('colonia', models.CharField(max_length=255)),
                ('municipio', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=255)),
                ('pais', models.CharField(max_length=255)),
                ('codigoPostal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TimbreFiscal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('selloCFD', models.TextField()),
                ('fechaTimbrado', models.TextField()),
                ('UUID', models.TextField()),
                ('numCertificadoSAT', models.TextField()),
                ('version', models.TextField()),
                ('selloSAT', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='comprobante',
            name='emisor',
            field=models.ForeignKey(to='invoices_Web.Emisor'),
        ),
        migrations.AddField(
            model_name='comprobante',
            name='receptor',
            field=models.ForeignKey(to='invoices_Web.Receptor'),
        ),
        migrations.AddField(
            model_name='comprobante',
            name='timbreFiscal',
            field=models.ForeignKey(to='invoices_Web.TimbreFiscal'),
        ),
    ]
