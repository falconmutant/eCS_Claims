from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

EVENT_TIPO = (
('C', 'Cita'),
('A', 'Ambulatorio'),
('H', 'Hospitalizacion'),
('U', 'Urgencia'),
)

EVENT_ESTATUS = (
('A', 'Abierto'),
('C', 'Cerrado'),
)

DX_ESTATUS = (
('A', 'Activo'),
('I', 'Inactivo'),
('R', 'Resuelto'),
)

class Proveedor(models.Model):
   owner = models.OneToOneField(User, null=True)
   rfc = models.CharField(max_length=13, null=False)
   cliente = models.CharField(max_length=255, null=False)
   org = models.CharField(max_length=255, null=False)
   hospital=models.CharField(max_length=255, null=False)
   localidad=models.CharField(max_length=255, null=False)


class Evento(models.Model):
   folioAut = models.CharField(max_length=255)
   numEvento = models.CharField(max_length=255)
   fechaAdm = models.DateTimeField()
   fechaAlta = models.DateTimeField()
   cedula = models.CharField(max_length=50)
   medico = models.CharField(max_length=255)
   tipo = models.CharField(choices=EVENT_TIPO, max_length=1)
   estatus = models.CharField(choices= EVENT_ESTATUS, max_length=1)
   proveedor = models.ForeignKey(Proveedor)
   total = models.DecimalField(max_digits=7, decimal_places=2)
   
class Paciente(models.Model):
   curp = models.CharField(max_length=18, null=False)
   fichaEmp = models.CharField(max_length=6, null=False)
   numCod = models.CharField(max_length=2, null=False)
   numEmpresa = models.CharField(max_length=6, null=False)
   nombre = models.CharField(max_length=255, null=False)
   evento = models.ForeignKey(Evento)

class Dx(models.Model):

   secuencia = models.PositiveSmallIntegerField()
   sistema = models.CharField(max_length=255)
   codigo = models.CharField(max_length=255)
   nombre = models.CharField(max_length=255)
   estatus = models.CharField(choices= DX_ESTATUS, max_length=1)
   evento = models.ForeignKey(Evento)

class Cargos(models.Model):
   evento = models.ForeignKey(Evento)
   secuencia = models.PositiveSmallIntegerField()
   fechaApli = models.DateTimeField()
   codigo = models.CharField(max_length=255)
   descripcion = models.CharField(max_length=255)
   udm = models.CharField(max_length=255)
   sistema = models.CharField(max_length=255)
   sistemaCodigo = models.CharField(max_length=255)
   cantidad = models.PositiveSmallIntegerField()
   precio = models.DecimalField(max_digits=7, decimal_places=2)
   subtotal = models.DecimalField(max_digits=7, decimal_places=2)
   iva = models.DecimalField(max_digits=7, decimal_places=2)
   descuento = models.DecimalField(max_digits=7, decimal_places=2)
   total = models.DecimalField(max_digits=7, decimal_places=2)


class CargosDx(models.Model):
   dx = models.ForeignKey(Dx)
   cargo = models.ForeignKey(Cargos)

class Autorizacion(models.Model):
   Estatus = models.CharField(max_length=255, null=False)
   FechaSolicitud = models.DateField()
   Comentarios  = models.CharField(max_length=255,null=True)
   TipoAprobacion = models.CharField(max_length=255)
   Sistema = models.CharField(max_length=255, null=False)
   evento = models.ForeignKey(Evento)
