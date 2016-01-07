from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Emisor(models.Model):
	rfc = models.CharField(max_length=13, null=False)
	nombre = models.CharField(max_length=255, null=False)
	calle = models.CharField(max_length=255, null=False)
	numExterior = models.IntegerField()
	colonia = models.CharField(max_length=255, null=False)
	municipio = models.CharField(max_length=255, null=False)
	estado = models.CharField(max_length=255, null=False)
	pais = models.CharField(max_length=255, null=False)
	codigoPostal = models.IntegerField()


class Receptor(models.Model):
	rfc = models.CharField(max_length=13, null=False)
	nombre = models.CharField(max_length=255, null=False)
	calle = models.CharField(max_length=255, null=False)
	numExterior = models.IntegerField()
	colonia = models.CharField(max_length=255, null=False)
	municipio = models.CharField(max_length=255, null=False)
	estado = models.CharField(max_length=255, null=False)
	pais = models.CharField(max_length=255, null=False)
	codigoPostal = models.IntegerField()

class TimbreFiscal(models.Model):
	selloCFD = models.TextField()
	fechaTimbrado = models.TextField()
	UUID = models.TextField()
	numCertificadoSAT = models.TextField()
	version = models.TextField()
	selloSAT = models.TextField()

class Comprobante(models.Model):
	version = models.CharField(max_length=5, null=False)
	serie = models.CharField(max_length=2, null=False)
	folio = models.CharField(max_length=255, null=False)
	fecha = models.DateTimeField()
	sello = models.TextField()
	formaPago = models.CharField(max_length=255, null=False)
	numCertificado = models.CharField(max_length=255, null=False)
	certificado = models.TextField()
	subtotal = models.DecimalField(max_digits=10, decimal_places=2)
	tipocambio = models.CharField(max_length=2, null=False)
	moneda = models.CharField(max_length=3, null=False)
	total = models.DecimalField(max_digits=10, decimal_places=2)
	tipocomprobante = models.CharField(max_length=255, null=False)
	metodopago = models.CharField(max_length=255, null=False)
	lugarexpedicion = models.CharField(max_length=255, null=False)
	numCtaPago = models.CharField(max_length=10, null=False)
	emisor = models.ForeignKey(Emisor)
	receptor = models.ForeignKey(Receptor)
	timbreFiscal = models.ForeignKey(TimbreFiscal)

class Conceptos(models.Model):
	cantidad = models.IntegerField()
	unidad = models.CharField(max_length=50, null=False)
	descripcion = models.CharField(max_length=255, null=False)
	valorUnitario = models.DecimalField(max_digits=10, decimal_places=2)
	importe = models.DecimalField(max_digits=10, decimal_places=2)
	comprobante = models.ForeignKey(Comprobante)

class Impuesto(models.Model):
	impuesto = models.CharField(max_length=10, null=False)
	tasa = models.IntegerField()
	importe = models.DecimalField(max_digits=10, decimal_places=2)
	comprobante = models.ForeignKey(Comprobante)



