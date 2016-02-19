from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from invoices_Web.models import Comprobante
import datetime
from django.conf import settings
from django.core.validators import RegexValidator

# Create your models here.

x = datetime.datetime.now()

EVENT_TIPO = (
('C', 'Cita'),
('A', 'Ambulatorio'),
('H', 'Hospitalizacion'),
('U', 'Urgencia'),
)

MEDICO_TIPO = (
('PC','Familiar'),
('RP','Referencia'),
('AP','Admision'),
('TP','Atencion'),
('CP','Consultor'),
('CO','Cobertura'),
('AS','Asistente'),
('AN','Anesteciologo'),
('IN','Interprete'),
('ER','Urgenciologo'),
('PP','Cirujano'),
)

YES_NO = (
('Y', 'Si'),
('N', 'No'),
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

AUTH_ESTATUS =(
('R', 'Recibido'),
('A', 'Aceptado PEMEX'),
('X', 'Rechazado PEMEX'),
('Y', 'Aceptado MAC'),
('N', 'Rechazado MAC'),
('E', 'En Revision MAC'),
('P', 'En Revision PEMEX'),
)


class Motivos(models.Model):
   motivo = models.CharField(max_length=255, null=False)
   is_active = models.CharField(null=False,max_length=1,choices= YES_NO)

class Localidad(models.Model):
   codigo = models.CharField(max_length=255, null=False)
   nombre = models.CharField(max_length=255, null=False)
   def __str__(self):
      return "%s" % (self.nombre)

class Proveedor(models.Model):
   phone_regex = RegexValidator(regex=r'^\+?1?\d{13}$', message="Numero debe ingresarse en formato internacional: '+521999999'. 14 digitos en total.")
   owner = models.OneToOneField(User, null=True)
   rfc = models.CharField(max_length=13, null=False)
   cliente = models.CharField(max_length=255, null=False)
   org = models.CharField(max_length=255, null=False)
   hospital=models.CharField(max_length=255, null=False)
   localidad=models.CharField(max_length=255, null=False)
   email = models.EmailField(max_length=70,blank=True)
   celular = models.CharField(max_length=14, validators=[phone_regex], blank=True) 
   whatsapp = models.CharField(choices= YES_NO,max_length=1,default='N')
   telegram = models.CharField(choices= YES_NO,max_length=1,default='N')
   sms = models.CharField(choices= YES_NO,max_length=1,default='N')
   tgcontacto = models.CharField(max_length=255, blank=True)
   def __str__(self):
      return "%s - %s" % (self.rfc, self.localidad)

class TipoUsuario(models.Model):
   MAC = 'M'
   PEMEX = 'P'
   ECARESOFT = 'E'
   SUPERUSER = 'S'
   TIPO_USER = (
      (MAC,'MAC'),
      (PEMEX,'PEMEX'),
      (ECARESOFT,'ECARESOFT'),
      (SUPERUSER,'SUPER USER'),
   )
   user = models.ForeignKey(User)
   tipo = models.CharField(choices=TIPO_USER,max_length=1)
   phone_regex = RegexValidator(regex=r'^\+?1?\d{13}$', message="Numero debe ingresarse en formato internacional: '+521999999'. 14 digitos en total.")
   email = models.EmailField(max_length=70,blank=True)
   celular = models.CharField(max_length=14, validators=[phone_regex], blank=True) 
   whatsapp = models.CharField(choices= YES_NO,max_length=1,default='N')
   telegram = models.CharField(choices= YES_NO,max_length=1,default='N')
   sms = models.CharField(choices= YES_NO,max_length=1,default='N')
   tgcontacto = models.CharField(max_length=255, blank=True)
   def __str__(self):
      return "%s" % (self.user.username)


class UsuarioLocalidad(models.Model):
   usuario = models.ForeignKey(User)
   localidad = models.ForeignKey(Localidad)
   def __str__(self):
      return "%s" % (self.usuario.username)

class Evento(models.Model):
   folioAut = models.CharField(max_length=255)
   numEvento = models.CharField(max_length=255)
   fechaAdm = models.DateTimeField()
   fechaAlta = models.DateTimeField()
   fechaPrimerCargo = models.DateTimeField(null=True)
   cedula = models.CharField(max_length=50)
   nommedico = models.CharField(max_length=255)
   tipo = models.CharField(choices=EVENT_TIPO, max_length=1)
   estatus = models.CharField(choices= EVENT_ESTATUS, max_length=1)
   proveedor = models.ForeignKey(Proveedor)
   total = models.DecimalField(max_digits=12, decimal_places=2)
   
class Paciente(models.Model):
   curp = models.CharField(max_length=18, null=False)
   fichaEmp = models.CharField(max_length=12, null=False)
   numCod = models.CharField(max_length=2, null=False)
   numEmpresa = models.CharField(max_length=6, null=False)
   nombre = models.CharField(max_length=255, null=False)
   evento = models.ForeignKey(Evento)

class Medico(models.Model):
   secuencia = models.PositiveSmallIntegerField()
   tipo = models.CharField(choices= MEDICO_TIPO, max_length=2)
   nombre = models.CharField(max_length=255)
   especialidad = models.CharField(max_length=255)
   cedula = models.CharField(max_length=255)
   evento = models.ForeignKey(Evento)

class Procedimiento(models.Model):
   secuencia = models.PositiveSmallIntegerField()
   sistema = models.CharField(max_length=255)
   codigo = models.CharField(max_length=255)
   nombre = models.CharField(max_length=255)
   fecha = models.DateField()
   observaciones = models.CharField(max_length=255,null=True)
   medico = models.ForeignKey(Medico)
   evento = models.ForeignKey(Evento)

class Dx(models.Model):

   secuencia = models.PositiveSmallIntegerField()
   sistema = models.CharField(max_length=255)
   codigo = models.CharField(max_length=255)
   nombre = models.CharField(max_length=255)
   estatus = models.CharField(choices= DX_ESTATUS, max_length=1)
   admision = models.CharField(choices= YES_NO,max_length=1,default='N')
   fecha = models.DateTimeField()
   observaciones = models.CharField(max_length=255,null=True)
   medico = models.ForeignKey(Medico,null=True)
   evento = models.ForeignKey(Evento)

class Cargo(models.Model):
   evento = models.ForeignKey(Evento)
   secuencia = models.PositiveSmallIntegerField()
   fechaApli = models.DateTimeField()
   codigo = models.CharField(max_length=255)
   descripcion = models.CharField(max_length=255)
   udm = models.CharField(max_length=255)
   sistema = models.CharField(max_length=255)
   sistemaCodigo = models.CharField(max_length=255)
   cantidad = models.PositiveSmallIntegerField()
   precio = models.DecimalField(max_digits=12, decimal_places=2)
   subtotal = models.DecimalField(max_digits=12, decimal_places=2)
   iva = models.DecimalField(max_digits=12, decimal_places=2)
   descuento = models.DecimalField(max_digits=12, decimal_places=2)
   total = models.DecimalField(max_digits=12, decimal_places=2)


class CargosDx(models.Model):
   dx = models.ForeignKey(Dx)
   cargo = models.ForeignKey(Cargo)

class Autorizacion(models.Model):
   estatus = models.CharField(choices= AUTH_ESTATUS, max_length=255, null=False)
   fechaSolicitud = models.DateField()
   comentarios  = models.CharField(max_length=255,null=True)
   tipoAprobacion = models.CharField(max_length=255)
   sistema = models.CharField(max_length=255, null=False)
   evento = models.ForeignKey(Evento,null=True)
   comprobante = models.ForeignKey(Comprobante,null=True)
   motivo = models.ForeignKey(Motivos, blank=True, null=True)
