import json
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib import auth
from .utils import *

from invoices_Web.models import *
from explorer.models import *
from claims.utils import sendNotifications


claim = Method()

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
	user = info(request)
	nombre_user = user.name

	total_claims = Autorizacion.objects.all().filter(TipoAprobacion='1').count()
	falta_claims = Autorizacion.objects.all().filter(Estatus__in=['E','R'],TipoAprobacion='1').count()
	resuelto_claims = total_claims-falta_claims

	total_invoices = Autorizacion.objects.all().filter(TipoAprobacion='2').count()
	falta_invoices = Autorizacion.objects.all().filter(Estatus__in=['E','R'],TipoAprobacion='2').count()
	resuelto_invoices = total_invoices-falta_invoices

	if user.type == TipoUsuario.MAC:
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

	if user.type == TipoUsuario.PEMEX:
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
	user = info(request)
	message_success=0
	message_error=1
	nombre_user = user.name
	detalle = claim.get_event_object(id)
	paciente = claim.get_patient_event(id)
	dx = claim.get_dx_event(id)
	cargo = claim.get_charge_event(id)
	proveedor = claim.get_provider_object(detalle.proveedor_id)
	medico = claim.get_medic_event(id)
	motivo = claim.get_cause()
	procedimiento = claim.get_process_event_medic(id,medico)



	if request.POST:
		estatus = request.POST.get('estatus')
		descripcion = request.POST.get('descripcion')
		motivo = request.POST.get('motivo')
		message_success=1
		return HttpResponseRedirect('/claims/')

	
	return render_to_response('claims/detalles.html',RequestContext(request,locals()))

@login_required
def detalle_historial(request, id):
	user = info(request)
	message_success=0
	message_error=1
	nombre_user = user.name
	detalle = claim.get_event_object(id)
	paciente = claim.get_patient_event(id)
	dx = claim.get_dx_event(id)
	cargo = claim.get_charge_event(id)
	proveedor = claim.get_provider_object(detalle.proveedor_id)
	medico = claim.get_medic_event(id)
	procedimiento = claim.get_process_event_medic(id,medico)

	return render_to_response('claims/historial_detalles.html',RequestContext(request,locals()))

@login_required
def claims(request):
	user = info(request)
	inicio,fin = user.date()
	nombre_user = user.name

	if user.type == TipoUsuario.MAC and user.type == TipoUsuario.PEMEX:
		localidad = claim.get_locality_user(user.id)
		proveedor= claim.get_providers_locality(localidad)
		evento = claim.get_event_provider(proveedor)
		paciente = claim.get_patient()
		cargo = claim.get_process_event(evento)
		motivo = claim.get_cause()
		
		autorizacion = claim.get_auth_type(user.type(),'claims',evento)
	else:
		proveedor = claim.get_providers()
		evento = claim.get_events()
		autorizacion = claim.get_auth_type(user.type(),'claims',evento)

	if request.POST:
		claim.set_date(request.POST.get("daterange").split(" - ")[0],request.POST.get("daterange").split(" - ")[1])
		autorizacion = claim.get_auth_filter(autorizacion,'date','')
		

	return render_to_response('claims/claims.html',RequestContext(request,locals()))

@login_required
def historial(request):
	user = info(request)
	nombre_user = user.name
	if user.type == TipoUsuario.MAC and user.type == TipoUsuario.PEMEX:
		localidad = claim.get_locality_user(user.id)
		proveedor= claim.get_providers_locality(localidad)
		evento = claim.get_event_provider(proveedor)
		paciente = claim.get_patient_event(evento)
		cargo = claim.get_process_event(evento)
		autorizacion = claim.get_auth_type(user.type(),'history',evento)
	else:
		proveedor = claim.get_providers()
		evento = claim.get_events()
		autorizacion = claim.get_auth_type(user.type(),'history',evento)
	
	return render_to_response('claims/historial.html',RequestContext(request,locals()))