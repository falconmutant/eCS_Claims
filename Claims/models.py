from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Cuenta(models.Model):
   folio = models.TextField()
   numEvento = models.TextField()
   fechaAdm = models.DateTimeField('')
   horaAdm = models.TextField()
   fechaAlta = models.DateTimeField('')
   horaAlta = models.TextField()
   medicoCedula = models.TextField()
   medicoId = models.TextField()
   estatus = models.TextField()


class Paciente(Models.Model):
   	curp = models.TextField()
   	fichaEmp = models.TextField()
   	numCod = models.TextField()
   	numEmpresa = models.TextField()
   	cuenta = models.ForeignKey(Cuenta)

class Proveedor(Models.Model):
	rfc = models.TextField()
	cliente = models.TextField()
	org = models.TextField()
   	cuenta = models.ForeignKey(Cuenta)

class Dx(Models.Model):
	sistema = models.TextField()
	dxvalue = models.TextField()
	estatus = models.TextField()
	cuerpo = models.TextField()
	cuenta = models.ForeignKey(Cuenta)

class Cargos(Models.Model):
	numEvento = models.TextField()
	secuencia = models.TextField()
	fechaApli = models.DateTimeField('')
	HoraApli = models.TextField()
	descripcion = models.TextField()
	descuento = models.TextField()
	udm = models.TextField()
	sistemacodigo = models.TextField()
	precio = models.TextField()
	subtotal = models.TextField()
	iva = models.TextField()
	descuento = models.TextField()
	total = models.TextField()
	dxrel = models.TextField()
	folioAuth = models.TextField()
	cuenta = models.ForeignKey(Cuenta)
	dx = models.ForeignKey(Dx)
