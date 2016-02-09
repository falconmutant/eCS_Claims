import json
from django.http import HttpResponseRedirect, HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib import auth
from django.views.generic import ListView
from claims.models import *
from invoices_Web.models import *
from explorer.models import *
from claims.utils import sendNotifications
import datetime

def index(request):
    return render_to_response('index.html',
        context_instance=RequestContext(request)
    )

def permisos(request):
	reportes = Query.objects.all()
	PemexPermisos = Permiso.objects.filter(usuario=TipoUsuario.PEMEX)
	MacPermisos = Permiso.objects.filter(usuario=TipoUsuario.MAC)
	return render_to_response('explorer/usuarios.html',
		RequestContext(request,locals()))


def save_permission(request):
	x = datetime.datetime.now()
	message_success = 0
	if x.month < 10:
		fecha = "%s-0%s-%s"% (x.year, x.month, x.day)
	else:
		fecha = "%s-%s-%s"% (x.year, x.month, x.day)
	if request.method == 'POST':
		query = int(request.POST.get("idquery"))
		selected = int(request.POST.get("select"))
		user = request.POST.get("user")
		if selected == 0:
			permiso = get_object_or_404(Permiso,usuario=user, reporte=query)
			permiso.delete()
		else:
			liga = Permiso(usuario=user, reporte=query,fecha=fecha)
			liga.save()
			message_success = 1
		PemexPermisos = Permiso.objects.filter(usuario=TipoUsuario.PEMEX)
		MacPermisos = Permiso.objects.filter(usuario=TipoUsuario.MAC)
		response_data = {}
		response_data['result'] = 'Create post successful! '
		response_data['message_success'] = message_success
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
	falta_claims = Autorizacion.objects.all().filter(Estatus__in=['E','R'],TipoAprobacion='1').count()
	resuelto_claims = total_claims-falta_claims

	total_invoices = Autorizacion.objects.all().filter(TipoAprobacion='2').count()
	falta_invoices = Autorizacion.objects.all().filter(Estatus__in=['E','R'],TipoAprobacion='2').count()
	resuelto_invoices = total_invoices-falta_invoices

	if tipouser.tipo == TipoUsuario.MAC:
		id_localidad = UsuarioLocalidad.objects.filter(usuario_id=request.user.id)
		localidad = Localidad.objects.filter(id__in=[locality_ids.localidad_id for locality_ids in id_localidad])
		proveedor = Proveedor.objects.filter(localidad__in=[locality.nombre for locality in localidad])
		evento = Evento.objects.filter(proveedor_id__in=[provider.id for provider in proveedor])

		total_claims = Autorizacion.objects.all().filter(TipoAprobacion='1',evento_id__in=[event.id for event in evento]).count()
		falta_claims = Autorizacion.objects.all().filter(Estatus__in=['E','R'],TipoAprobacion='1',evento_id__in=[event.id for event in evento]).count()
		resuelto_claims = total_claims-falta_claims

		emisor = Emisor.objects.filter(rfc__in=[provider.rfc for provider in proveedor])
		comprobantes = Comprobante.objects.filter(emisor_id__in=[trans.id for trans in emisor])

		total_invoices = Autorizacion.objects.all().filter(TipoAprobacion='2',comprobante_id__in=[vouchers.id for vouchers in comprobantes]).count()
		falta_invoices = Autorizacion.objects.all().filter(Estatus__in=['E','R'],TipoAprobacion='2',comprobante_id__in=[vouchers.id for vouchers in comprobantes]).count()
		resuelto_invoices = total_invoices-falta_invoices

	if tipouser.tipo == TipoUsuario.PEMEX:
		id_localidad = UsuarioLocalidad.objects.filter(usuario_id=request.user.id)
		localidad = Localidad.objects.filter(id__in=[locality_ids.localidad_id for locality_ids in id_localidad])
		proveedor = Proveedor.objects.filter(localidad__in=[locality.nombre for locality in localidad])
		evento = Evento.objects.filter(proveedor_id__in=[provider.id for provider in proveedor])

		total_claims = Autorizacion.objects.all().filter(TipoAprobacion='1',evento_id__in=[event.id for event in evento]).count()
		falta_claims = Autorizacion.objects.all().filter(Estatus__in=['Y','P'],TipoAprobacion='1',evento_id__in=[event.id for event in evento]).count()
		resuelto_claims = total_claims-falta_claims

		emisor = Emisor.objects.filter(rfc__in=[provider.rfc for provider in proveedor])
		comprobantes = Comprobante.objects.filter(emisor_id__in=[trans.id for trans in emisor])

		total_invoices = Autorizacion.objects.all().filter(TipoAprobacion='2',comprobante_id__in=[vouchers.id for vouchers in comprobantes]).count()
		falta_invoices = Autorizacion.objects.all().filter(Estatus__in=['Y','P'],TipoAprobacion='2',comprobante_id__in=[vouchers.id for vouchers in comprobantes]).count()
		resuelto_invoices = total_invoices-falta_invoices
	
	return render_to_response('pantallas.html',RequestContext(request,locals()))

@login_required
def detalle(request, id):
	message_success=0
	message_error=1
	tipouser = get_object_or_404(TipoUsuario,user_id=request.user.id)
	if request.POST:
		estatus = request.POST.get('estatus')
		descripcion = request.POST.get('descripcion')
		motivo = request.POST.get('motivo')
		Autorizacion.objects.filter(evento_id=id).update(Estatus=estatus,Comentarios=descripcion,motivo=motivo)
		message_success=1
		try:
			if estatus == 'Y':
				detalle = get_object_or_404(Evento, id=id)
				locality = UsuarioLocalidad.objects.filter(usuario = request.user.id)
				for localitys in locality:
					message = 'Se ha Autorizado el Estado de Cuenta {0}, por el sectorial MAC. Favor de revisar Sistema'.format(detalle.folioAut)
					sendNotifications(localitys.localidad,message, TipoUsuario.PEMEX)
			if estatus == 'A':
				detalle = get_object_or_404(Evento, id=id)
				locality = UsuarioLocalidad.objects.filter(usuario = request.user.id)
				for localitys in locality:
					message = 'Se ha Autorizado el Estado de Cuenta {0}, por el sectorial PEMEX.'.format(detalle.folioAut)
					sendNotifications(localitys.localidad,message, TipoUsuario.MAC)
		except Exception, e:
			message_error = 1

		x = datetime.datetime.now()
		if x.month < 10:
			inicio = "%s-0%s-%s"% (x.year, x.month, x.day)
			fin = "%s-0%s-%s"% (x.year, x.month, x.day)
		else:
			inicio = "%s-%s-%s"% (x.year, x.month, x.day)
			fin = "%s-%s-%s"% (x.year, x.month, x.day)
		nombre_user = request.user.get_full_name()

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
	id_localidad = UsuarioLocalidad.objects.filter(usuario_id=request.user.id)
	localidad = Localidad.objects.filter(id__in=[locality_ids.localidad_id for locality_ids in id_localidad])
	proveedor = Proveedor.objects.filter(localidad__in=[locality.nombre for locality in localidad])
	evento = Evento.objects.filter(proveedor_id__in=[provider.id for provider in proveedor])
	paciente = Paciente.objects.filter(evento_id__in=[event.id for event in evento])
	cargo = Cargo.objects.filter(evento_id__in=[event.id for event in evento])
	if tipouser.tipo == TipoUsuario.MAC:
		autorizacion = Autorizacion.objects.all().filter(Estatus__in=['E','R'],TipoAprobacion='1',evento_id__in=[event.id for event in evento])
	if tipouser.tipo == TipoUsuario.PEMEX:
		autorizacion = Autorizacion.objects.all().filter(Estatus__in=['Y','P'],TipoAprobacion='1',evento_id__in=[event.id for event in evento])
	if tipouser.tipo == TipoUsuario.ECARESOFT:
		autorizacion = Autorizacion.objects.all().filter(Estatus__in=['E','R','A','P'],TipoAprobacion='1')
	if tipouser.tipo == TipoUsuario.SUPERUSER:
		autorizacion = Autorizacion.objects.all().filter(Estatus__in=['E','R','A','P'],TipoAprobacion='1')
	
	if request.POST:
		inicio = request.POST.get("daterange").split(" - ")[0]
		fin = request.POST.get("daterange").split(" - ")[1]
		if tipouser.tipo == TipoUsuario.MAC:
			autorizacion = autorizacion.filter(FechaSolicitud__range=[inicio, fin])
		if tipouser.tipo == TipoUsuario.PEMEX:
			autorizacion = autorizacion.filter(FechaSolicitud__range=[inicio, fin])
		if tipouser.tipo == TipoUsuario.ECARESOFT:
			autorizacion = autorizacion.filter(FechaSolicitud__range=[inicio, fin])
		if tipouser.tipo == TipoUsuario.SUPERUSER:
			autorizacion = autorizacion.filter(FechaSolicitud__range=[inicio, fin])	
		inicio = inicio
		fin = fin

	return render_to_response('claims/claims.html',RequestContext(request,locals()))

@login_required
def historial(request):
	nombre_user = request.user.get_full_name()
	tipouser = get_object_or_404(TipoUsuario,user_id=request.user.id)
	id_localidad = UsuarioLocalidad.objects.filter(usuario_id=request.user.id)
	localidad = Localidad.objects.filter(id__in=[locality_ids.localidad_id for locality_ids in id_localidad])
	proveedor = Proveedor.objects.filter(localidad__in=[locality.nombre for locality in localidad])
	evento = Evento.objects.filter(proveedor_id__in=[provider.id for provider in proveedor])
	paciente = Paciente.objects.filter(evento_id__in=[event.id for event in evento])
	cargo = Cargo.objects.filter(evento_id__in=[event.id for event in evento])
	if tipouser.tipo == TipoUsuario.MAC:
		autorizacion = Autorizacion.objects.all().filter(Estatus__in=['A','X','Y','N','P'],TipoAprobacion='1',evento_id__in=[event.id for event in evento])
	if tipouser.tipo == TipoUsuario.PEMEX:
		autorizacion = Autorizacion.objects.all().filter(Estatus__in=['X'],TipoAprobacion='1',evento_id__in=[event.id for event in evento])
	if tipouser.tipo == TipoUsuario.ECARESOFT:
		autorizacion = Autorizacion.objects.all().filter(TipoAprobacion='1')
	if tipouser.tipo == TipoUsuario.SUPERUSER:
		autorizacion = Autorizacion.objects.all().filter(TipoAprobacion='1')
    	return render_to_response('claims/historial.html',RequestContext(request,locals()))