from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Autorizaciones(models.Model):
   Folio = models.CharField(max_length=255)
   IdEvento = models.ForeignKey(Evento)
   Estatus = models.CharField(max_length=255, null=False)
   FechaSolicitud = models.DateTimeField()
   TipoAprobacion = models.CharField(max_length=255)
   Comentarios = models.CharField(max_length=255, null=False)

class Paciente(models.Model):
   Nombre = models.CharField(max_length=255, null=False)
   PesoEstatura = models.CharField(max_length=255, null=False)
   FechanNacimiento = models.DateTimeField()
   Sexo = models.CharField(max_length=255, null=False)

class Medico(models.Model):
   Nombre = models.CharField(max_length=255, null=False)
   Especialidad = models.CharField(max_length=255, null=False)
   Cedula = models.CharField(max_length=255, null=False)


class Evento(models.Model):
   IdPaciente = models.ForeignKey(Paciente)
   IdMedico = models.ForeignKey(Medico)
   Diagnostico = models.CharField(max_length=255, null=False)
   IdCargo = models.ForeignKey(Cargo)
   IdTipoServicio = models.ForeignKey(TipoServicio)
   IdProveedor = models.ForeignKey(Proveedor)
   FechaAdmision = models.DateTimeField()
   FechaSalida = models.DateTimeField()

class Cargo(models.Model):
   Descripcion = models.CharField(max_length=255, null=False)
   IdTipoCargo = models.ForeignKey(TipoCargo)
   Cantidad = models.IntegerField(null=False)
   PrecioUnitario = models.DecimalField(null=False)
   Descuento = models.DecimalField(null=False)
   PrecioNeto = models.DecimalField(null=False)
   Impuesto = models.DecimalField(null=False)
   FechaAplicacion = models.DateTimeField()
   HoraAplicacion = models.CharField(max_length=255, null=False)

class CargoPorEvento(models.Model):
   IdEvento = models.ForeignKey(Evento)
   IdCargo = models.ForeignKey(Cargo)

class Proveedor(models.Model):
   Proveedor = models.CharField(max_length=255, null=False)
   Localidad = models.CharField(max_length=255, null=False)

class TipoServicio(models.Model):
   Nombre = models.CharField(max_length=255, null=False)

class TipoCargo(models.Model):
   Nombre = models.CharField(max_length=255, null=False)

