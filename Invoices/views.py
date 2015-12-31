from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from Claims.models import *
import datetime

@login_required
def detalle(request, id):
	idd=id
	bandera=0
	if request.POST:
		estatus = request.POST.get('estatus')
		descripcion = request.POST.get('descripcion')
		Autorizacion.objects.filter(id=idd).update(Estatus=estatus,Comentarios=descripcion)
		bandera=1
		nombre = request.user.get_full_name()
		autorizacion = Autorizacion.objects.all().filter(Estatus='Recibido',TipoAprobacion='2')
		cuenta = Cuenta.objects.all()
		paciente = Paciente.objects.all()
		proveedor = Proveedor.objects.all()
		cargo = Cargo.objects.all()
		return render_to_response('invoices/invoices.html',RequestContext(request,locals()))
	nombre = request.user.get_full_name()
	detalle = get_object_or_404(Cuenta, id=id)
	paciente = Paciente.objects.all()
	medico = Medico.objects.all()
	cargo = Cargo.objects.all()
	return render_to_response('invoices/detalles.html',RequestContext(request,locals()))

@login_required
def invoices(request):
	x = datetime.datetime.now()
	inicio = "%s-%s-%s"% (x.year, x.month, x.day)
	fin = "%s-%s-%s"% (x.year, x.month, x.day)
	nombre = request.user.get_full_name()
	autorizacion = Autorizacion.objects.all().filter(Estatus='Recibido',TipoAprobacion='2')
	cuenta = Cuenta.objects.all()
	proveedor = Proveedor.objects.all()
	medico = Medico.objects.all()
	cargo = Cargo.objects.all()
	if request.POST:
		autorizacion = Autorizacion.objects.all().filter(Estatus='Recibido',TipoAprobacion='2',FechaSolicitud__range=[request.POST.get("inicio"), request.POST.get("fin")])
		if request.POST.get("tipo") != 'vacio':
			autorizacion = Autorizacion.objects.all().filter(Sistema=request.POST.get("tipo"),TipoAprobacion='2')
		if request.POST.get("cliente") != 'vacio':
			cuenta = Cuenta.objects.all().filter(IdProveedor_id=request.POST.get("cliente"))
		inicio = request.POST.get("inicio")
		fin = request.POST.get("fin")
    	return render_to_response('invoices/invoices.html',RequestContext(request,locals()))

@login_required
def historial(request):
	nombre = request.user.get_full_name()
	autorizacion = Autorizacion.objects.all().filter(TipoAprobacion='2')
	cuenta = Cuenta.objects.all()
	paciente = Paciente.objects.all()
	proveedor = Proveedor.objects.all()
	cargo = Cargo.objects.all()
    	return render_to_response('invoices/historial.html',RequestContext(request,locals()))