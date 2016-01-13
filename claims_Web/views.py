from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from claims.models import *
import datetime

def index(request):
    return render_to_response('index.html',
        context_instance=RequestContext(request)
    )


@login_required
def logged_in(request):
	nombre = request.user.get_full_name()
	return render_to_response('pantallas.html',RequestContext(request,locals()))

@login_required
def detalle(request, id):
	idd=id
	bandera=0
	if request.POST:
		estatus = request.POST.get('estatus')
		descripcion = request.POST.get('descripcion')
		motivo = request.POST.get('motivo')
		Autorizacion.objects.filter(evento_id=idd).update(Estatus=estatus,Comentarios=descripcion,motivo=motivo)
		bandera=1
		x = datetime.datetime.now()
		if x.month < 10:
			inicio = "%s-0%s-%s"% (x.year, x.month, x.day)
			fin = "%s-0%s-%s"% (x.year, x.month, x.day)
		else:
			inicio = "%s-%s-%s"% (x.year, x.month, x.day)
			fin = "%s-%s-%s"% (x.year, x.month, x.day)
		nombre = request.user.get_full_name()
		autorizacion = Autorizacion.objects.all().filter(Estatus='R',TipoAprobacion='1')
		evento = Evento.objects.all()
		paciente = Paciente.objects.all()
		proveedor = Proveedor.objects.all()
		cargo = Cargos.objects.all()
		dx = Dx.objects.all()
		return render_to_response('claims/claims.html',RequestContext(request,locals()))
	nombre = request.user.get_full_name()
	dx = Dx.objects.all()
	detalle = get_object_or_404(Evento, id=id)
	paciente = Paciente.objects.all()
	cargo = Cargos.objects.all()
	proveedor = Proveedor.objects.all()
	motivo = Motivos.objects.all()
	return render_to_response('claims/detalles.html',RequestContext(request,locals()))

@login_required
def detalle_historial(request, id):
	nombre = request.user.get_full_name()
	dx = Dx.objects.all()
	detalle = get_object_or_404(Evento, id=id)
	paciente = Paciente.objects.all()
	cargo = Cargos.objects.all()
	proveedor = Proveedor.objects.all()
	motivo = Motivos.objects.all()
	return render_to_response('claims/historial_detalles.html',RequestContext(request,locals()))

@login_required
def claims(request):
	x = datetime.datetime.now()
	if x.month < 10:
		inicio = "%s-0%s-%s"% (x.year, x.month, x.day)
		fin = "%s-0%s-%s"% (x.year, x.month, x.day)
	else:
		inicio = "%s-%s-%s"% (x.year, x.month, x.day)
		fin = "%s-%s-%s"% (x.year, x.month, x.day)
	nombre = request.user.get_full_name()

	autorizacion = Autorizacion.objects.all().filter(Estatus='R',TipoAprobacion='1')
	evento = Evento.objects.all()
	paciente = Paciente.objects.all()
	proveedor = Proveedor.objects.all()
	cargo = Cargos.objects.all()
	if request.POST:
		autorizacion = Autorizacion.objects.all().filter(Estatus='R',TipoAprobacion='1',FechaSolicitud__range=[request.POST.get("inicio"), request.POST.get("fin")])
		if request.POST.get("tipo") != 'vacio':
			autorizacion = Autorizacion.objects.all().filter(Sistema=request.POST.get("tipo"),TipoAprobacion='1')
		if request.POST.get("cliente") != 'vacio':
			evento = Evento.objects.all().filter(proveedor_id=request.POST.get("cliente"))
		inicio = request.POST.get("inicio")
		fin = request.POST.get("fin")

    	return render_to_response('claims/claims.html',RequestContext(request,locals()))

@login_required
def historial(request):
	nombre = request.user.get_full_name()
	autorizacion = Autorizacion.objects.all().filter(TipoAprobacion='1').exclude(Estatus='R')
	evento = Evento.objects.all()
	paciente = Paciente.objects.all()
	proveedor = Proveedor.objects.all()
	cargo = Cargos.objects.all()
    	return render_to_response('claims/historial.html',RequestContext(request,locals()))