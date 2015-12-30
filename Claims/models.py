from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Paciente(models.Model):
   Nombre = models.CharField(max_length=255, null=False)
   CURP = models.CharField(max_length=18, null=False)
   FichaEmpleado = models.CharField(max_length=255, null=False)
   NumeroEmpresa = models.CharField(max_length=255, null=False)
   PesoEstatura = models.CharField(max_length=255, null=False)
   FechaNacimiento = models.TimeField()
   Sexo = models.CharField(max_length=255, null=False)

class Medico(models.Model):
   Nombre = models.CharField(max_length=255, null=False)
   Especialidad = models.CharField(max_length=255, null=False)
   Cedula = models.CharField(max_length=255, null=False)
   RFC = models.CharField(max_length=13, null=False)

class Proveedor(models.Model):
   RFC = models.CharField(max_length=13, null=False)
   Cliente = models.CharField(max_length=255, null=False)
   Organizacion = models.CharField(max_length=255, null=False)
   Localidad = models.CharField(max_length=255, null=False)

class Cuenta(models.Model):
   IdPaciente = models.ForeignKey(Paciente)
   IdMedico = models.ForeignKey(Medico)
   IdProveedor = models.ForeignKey(Proveedor)
   Diagnostico = models.CharField(max_length=255, null=False)
   FechaAdmision = models.DateTimeField()
   FechaAlta = models.DateTimeField()

class Cargo(models.Model):
   IdCuenta = models.ForeignKey(TipoCargo)
   Descripcion = models.CharField(max_length=255, null=False)
   UnidadDeMedida = models.CharField(max_length=255, null=False)
   Cantidad = models.IntegerField(null=False)
   PrecioUnitario = models.DecimalField(max_digits=10, decimal_places=2)
   Descuento = models.DecimalField(max_digits=10, decimal_places=2)
   PrecioNeto = models.DecimalField(max_digits=10, decimal_places=2)
   Impuesto = models.DecimalField(max_digits=10, decimal_places=2)
   FechaAplicacion = models.DateTimeField()

class Autorizacion(models.Model):
   Folio = models.CharField(max_length=255, null=False)
   IdCuenta = models.ForeignKey(Cuenta)
   Estatus = models.CharField(max_length=255, null=False)
   FechaSolicitud = models.TimeField()
   Comentarios  = models.CharField(max_length=255)
   TipoAprobacion = models.CharField(max_length=255)
   Sistema = models.CharField(max_length=255, null=False)
