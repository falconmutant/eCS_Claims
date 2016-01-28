import json
from django.http import HttpResponseRedirect, HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib import auth
from claims.models import *
from explorer.models import *
import datetime

def index(request):
    return render_to_response('index.html',
        context_instance=RequestContext(request)
    )


def permisos(request):
	reportes = Query.objects.all()
	PemexPermisos = Permiso.objects.filter(usuario='P')
	MacPermisos = Permiso.objects.filter(usuario='M')
	return render_to_response('explorer/usuarios.html',
		RequestContext(request,locals()))

def save_permission(request):
    if request.method == 'POST':
    	query = int(request.POST.get("idquery"))
    	selected = int(request.POST.get("select"))
    	user = request.POST.get("user")
    	permiso = get_object_or_404(Permiso,usuario=user, reporte=query)
    	if selected == 0:
    		liga = Permiso(usuario=user, reporte=query)
    		liga.save()
    	else:
    		permiso.delete()
    		response_data = {}
    		response_data['result'] = 'Create post successful! '
    		return HttpResponse(
    			json.dumps(response_data),
    			content_type="application/json"
    		)
    else:
    	return HttpResponse(
    		json.dumps({"nothing to see": "this isn't happening"}),
    		content_type="application/json"
    	)

@login_required
def logged_in(request):
	nombre_user = request.user.get_full_name()
	tipouser = get_object_or_404(TipoUsuario,user_id=request.user.id)
	total_claims = Autorizacion.objects.all().filter(TipoAprobacion='1').count()
	falta_claims = Autorizacion.objects.all().filter(Estatus='R',TipoAprobacion='1').count()
	resuelto_claims = total_claims-falta_claims
	total_invoices = Autorizacion.objects.all().filter(TipoAprobacion='2').count()
	falta_invoices = Autorizacion.objects.all().filter(Estatus='R',TipoAprobacion='2').count()
	resuelto_invoices = total_invoices-falta_invoices
	return render_to_response('pantallas.html',RequestContext(request,locals()))

@login_required
def detalle(request, id):
	idd=id
	bandera=0
	tipouser = get_object_or_404(TipoUsuario,user_id=request.user.id)
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
		nombre_user = request.user.get_full_name()
		
		if tipouser.tipo == 'M':
			autorizacion = Autorizacion.objects.all().filter(Estatus__in=['E','R'],TipoAprobacion='1')
		if tipouser.tipo == 'P':
			autorizacion = Autorizacion.objects.all().filter(Estatus__in=['Y','P'],TipoAprobacion='1')
		if tipouser.tipo == 'E':
			autorizacion = Autorizacion.objects.all().filter(Estatus__in=['E','R','A','P'],TipoAprobacion='1')
		if tipouser.tipo == 'S':
			autorizacion = Autorizacion.objects.all().filter(Estatus__in=['E','R','A','P'],TipoAprobacion='1')
		evento = Evento.objects.filter(id__in=[auth.evento_id for auth in autorizacion])
		paciente = Paciente.objects.filter(evento_id__in=[event.id for event in evento])
		proveedor = Proveedor.objects.filter(id__in=[event.proveedor_id for event in evento])
		cargo = Cargo.objects.filter(evento_id__in=[event.id for event in evento])
		dx = Dx.objects.filter(evento_id__in=[event.id for event in evento])
		return HttpResponseRedirect('/claims/')

	nombre_user = request.user.get_full_name()
	detalle = get_object_or_404(Evento, id=id)
	paciente = get_object_or_404(Paciente, evento=id)
	dx = Dx.objects.filter(evento_id=detalle.id)
	cargo = Cargo.objects.filter(evento_id=detalle.id)
	proveedor = get_object_or_404(Proveedor, id=detalle.proveedor_id)
	medico = Medico.objects.filter(evento_id=detalle.id)
	procedimiento = Procedimiento.objects.filter(evento_id=detalle.id,medico_id__in=[doctor.id for doctor in medico])
	motivo = Motivos.objects.all()
	return render_to_response('claims/detalles.html',RequestContext(request,locals()))

@login_required
def detalle_historial(request, id):
	nombre_user = request.user.get_full_name()
	detalle = get_object_or_404(Evento, id=id)
	paciente = get_object_or_404(Paciente, evento=id)
	dx = Dx.objects.filter(evento_id=detalle.id)
	cargo = Cargo.objects.filter(evento_id=detalle.id)
	proveedor = get_object_or_404(Proveedor, id=detalle.proveedor_id)
	medico = Medico.objects.filter(evento_id=detalle.id)
	procedimiento = Procedimiento.objects.filter(evento_id=detalle.id,medico_id__in=[doctor.id for doctor in medico])
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
	nombre_user = request.user.get_full_name()
	tipouser = get_object_or_404(TipoUsuario,user_id=request.user.id)
	if tipouser.tipo == 'M':
		autorizacion = Autorizacion.objects.all().filter(Estatus__in=['E','R'],TipoAprobacion='1')
	if tipouser.tipo == 'P':
		autorizacion = Autorizacion.objects.all().filter(Estatus__in=['Y','P'],TipoAprobacion='1')
	if tipouser.tipo == 'E':
		autorizacion = Autorizacion.objects.all().filter(Estatus__in=['E','R','A','P'],TipoAprobacion='1')
	if tipouser.tipo == 'S':
		autorizacion = Autorizacion.objects.all().filter(Estatus__in=['E','R','A','P'],TipoAprobacion='1')
	evento = Evento.objects.filter(id__in=[auth.evento_id for auth in autorizacion])
	paciente = Paciente.objects.filter(evento_id__in=[event.id for event in evento])
	proveedor = Proveedor.objects.filter(id__in=[event.proveedor_id for event in evento])
	cargo = Cargo.objects.filter(evento_id__in=[event.id for event in evento])
	if request.POST:
		inicio = request.POST.get("daterange").split(" - ")[0]
		fin = request.POST.get("daterange").split(" - ")[1]
		if tipouser.tipo == 'M':
			autorizacion = Autorizacion.objects.all().filter(Estatus__in=['E','R'],TipoAprobacion='1',FechaSolicitud__range=[inicio, fin])
		if tipouser.tipo == 'P':
			autorizacion = Autorizacion.objects.all().filter(Estatus__in=['Y','P'],TipoAprobacion='1',FechaSolicitud__range=[inicio, fin])
		if tipouser.tipo == 'E':
			autorizacion = Autorizacion.objects.all().filter(Estatus__in=['E','R','A','P'],TipoAprobacion='1',FechaSolicitud__range=[inicio, fin])
		if tipouser.tipo == 'S':
			autorizacion = Autorizacion.objects.all().filter(Estatus__in=['E','R','A','P'],TipoAprobacion='1',FechaSolicitud__range=[inicio, fin])	
		inicio = inicio
		fin = fin

	return render_to_response('claims/claims.html',RequestContext(request,locals()))

@login_required
def historial(request):
	nombre_user = request.user.get_full_name()
	tipouser = get_object_or_404(TipoUsuario,user_id=request.user.id)
	if tipouser.tipo == 'M':
		autorizacion = Autorizacion.objects.all().filter(Estatus__in=['A','X','Y','N','P'],TipoAprobacion='1')
	if tipouser.tipo == 'P':
		autorizacion = Autorizacion.objects.all().filter(Estatus__in=['X'],TipoAprobacion='1')
	if tipouser.tipo == 'E':
		autorizacion = Autorizacion.objects.all().filter(TipoAprobacion='1')
	if tipouser.tipo == 'S':
		autorizacion = Autorizacion.objects.all().filter(TipoAprobacion='1')
	evento = Evento.objects.filter(id__in=[auth.evento_id for auth in autorizacion])
	paciente = Paciente.objects.filter(evento_id__in=[event.id for event in evento])
	proveedor = Proveedor.objects.filter(id__in=[event.proveedor_id for event in evento])
	cargo = Cargo.objects.filter(evento_id__in=[event.id for event in evento])
    	return render_to_response('claims/historial.html',RequestContext(request,locals()))