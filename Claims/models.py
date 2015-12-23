from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Paciente(models.Model):
   Nombre = models.CharField(max_length=255, null=False)
   PesoEstatura = models.CharField(max_length=255, null=False)
   FechanNacimiento = models.DateTimeField()
   Sexo = models.CharField(max_length=255, null=False)

class Medico(models.Model):
   Nombre = models.CharField(max_length=255, null=False)
   Especialidad = models.CharField(max_length=255, null=False)
   Cedula = models.CharField(max_length=255, null=False)

class TipoCargo(models.Model):
   Nombre = models.CharField(max_length=255, null=False)

class Cargo(models.Model):
   Descripcion = models.CharField(max_length=255, null=False)
   IdTipoCargo = models.ForeignKey(TipoCargo)
   Cantidad = models.IntegerField(null=False)
   PrecioUnitario = models.DecimalField(max_digits=10, decimal_places=2)
   Descuento = models.DecimalField(max_digits=10, decimal_places=2)
   PrecioNeto = models.DecimalField(max_digits=10, decimal_places=2)
   Impuesto = models.DecimalField(max_digits=10, decimal_places=2)
   FechaAplicacion = models.DateTimeField()
   HoraAplicacion = models.CharField(max_length=255, null=False)

class TipoServicio(models.Model):
   Nombre = models.CharField(max_length=255, null=False)

class Proveedor(models.Model):
   Proveedor = models.CharField(max_length=255, null=False)
   Localidad = models.CharField(max_length=255, null=False)

class Evento(models.Model):
   IdPaciente = models.ForeignKey(Paciente)
   IdMedico = models.ForeignKey(Medico)
   Diagnostico = models.CharField(max_length=255, null=False)
   IdTipoServicio = models.ForeignKey(TipoServicio)
   IdProveedor = models.ForeignKey(Proveedor)
   FechaAdmision = models.DateTimeField()
   FechaSalida = models.DateTimeField()

class Autorizaciones(models.Model):
   Folio = models.CharField(max_length=255)
   IdEvento = models.ForeignKey(Evento)
   Estatus = models.CharField(max_length=255, null=False)
   FechaSolicitud = models.DateTimeField()
   TipoAprobacion = models.CharField(max_length=255)
   Comentarios = models.CharField(max_length=255, null=False)

class CargoPorEvento(models.Model):
   IdEvento = models.ForeignKey(Evento)
   IdCargo = models.ForeignKey(Cargo)