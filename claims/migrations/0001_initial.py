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
            name='Cargos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('secuencia', models.PositiveSmallIntegerField()),
                ('fechaApli', models.DateTimeField()),
                ('codigo', models.CharField(max_length=255)),
                ('descripcion', models.CharField(max_length=255)),
                ('udm', models.CharField(max_length=255)),
                ('sistemaCodificacion', models.CharField(max_length=255)),
                ('cantidad', models.PositiveSmallIntegerField()),
                ('precio', models.DecimalField(max_digits=7, decimal_places=2)),
                ('subtotal', models.DecimalField(max_digits=7, decimal_places=2)),
                ('iva', models.DecimalField(max_digits=7, decimal_places=2)),
                ('descuento', models.DecimalField(max_digits=7, decimal_places=2)),
                ('total', models.DecimalField(max_digits=7, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Dx',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('secuencia', models.PositiveSmallIntegerField()),
                ('sistema', models.CharField(max_length=255)),
                ('dxvalue', models.CharField(max_length=255)),
                ('estatus', models.CharField(max_length=1, choices=[('Y', 'Activo'), ('N', 'Inactivo')])),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('folioAut', models.CharField(max_length=255)),
                ('numEvento', models.CharField(max_length=255)),
                ('fechaAdm', models.DateTimeField()),
                ('fechaAlta', models.DateTimeField()),
                ('cedula', models.CharField(max_length=50)),
                ('medico', models.CharField(max_length=255)),
                ('tipo', models.CharField(max_length=1, choices=[('C', 'Cita'), ('A', 'Ambulatorio'), ('H', 'Hospitalizacion'), ('U', 'Urgencia')])),
                ('estatus', models.CharField(max_length=1, choices=[('A', 'Abierto'), ('C', 'Cerrado')])),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('curp', models.CharField(max_length=18)),
                ('fichaEmp', models.CharField(max_length=6)),
                ('numCod', models.CharField(max_length=2)),
                ('numEmpresa', models.CharField(max_length=6)),
                ('nombre', models.CharField(max_length=255)),
                ('evento', models.ForeignKey(to='claims.Evento')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rfc', models.CharField(max_length=13)),
                ('cliente', models.CharField(max_length=255)),
                ('org', models.CharField(max_length=255)),
                ('owner', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='evento',
            name='proveedor',
            field=models.ForeignKey(to='claims.Proveedor'),
        ),
        migrations.AddField(
            model_name='dx',
            name='evento',
            field=models.ForeignKey(to='claims.Evento'),
        ),
        migrations.AddField(
            model_name='cargos',
            name='dx',
            field=models.ForeignKey(to='claims.Dx'),
        ),
        migrations.AddField(
            model_name='cargos',
            name='evento',
            field=models.ForeignKey(to='claims.Evento'),
        ),
    ]
