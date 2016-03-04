import json
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
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
from .utils import *



# Create your views here.
def index(request):
    return render_to_response('index.html',
        context_instance=RequestContext(request)
    )

@login_required
def logged_in(request):
	user = info(request)
	user_type = user.type()
	user_name = user.name()
	permission = user.permission(user_type)

	total_claims = Autorizacion.objects.all().filter(tipoAprobacion='1').count()
	falta_claims = Autorizacion.objects.all().filter(estatus__in=['E','R'],tipoAprobacion='1').count()
	resuelto_claims = total_claims-falta_claims

	total_invoices = Autorizacion.objects.all().filter(tipoAprobacion='2').count()
	falta_invoices = Autorizacion.objects.all().filter(estatus__in=['E','R'],tipoAprobacion='2').count()
	resuelto_invoices = total_invoices-falta_invoices

	if user.type() == TipoUsuario.MAC:
		id_localidad = UsuarioLocalidad.objects.filter(usuario_id=request.user.id)
		localidad = Localidad.objects.filter(id__in=[locality_ids.localidad_id for locality_ids in id_localidad])
		proveedor = Proveedor.objects.filter(localidad__in=[locality.nombre for locality in localidad])
		evento = Evento.objects.filter(proveedor_id__in=[provider.id for provider in proveedor])

		total_claims = Autorizacion.objects.all().filter(tipoAprobacion='1',evento_id__in=[event.id for event in evento]).count()
		falta_claims = Autorizacion.objects.all().filter(estatus__in=['E','R'],tipoAprobacion='1',evento_id__in=[event.id for event in evento]).count()
		resuelto_claims = total_claims-falta_claims

		emisor = Emisor.objects.filter(rfc__in=[provider.rfc for provider in proveedor])
		comprobantes = Comprobante.objects.filter(emisor_id__in=[trans.id for trans in emisor])

		total_invoices = Autorizacion.objects.all().filter(tipoAprobacion='2',comprobante_id__in=[vouchers.id for vouchers in comprobantes]).count()
		falta_invoices = Autorizacion.objects.all().filter(estatus__in=['E','R'],tipoAprobacion='2',comprobante_id__in=[vouchers.id for vouchers in comprobantes]).count()
		resuelto_invoices = total_invoices-falta_invoices

	if user.type() == TipoUsuario.PEMEX:
		id_localidad = UsuarioLocalidad.objects.filter(usuario_id=request.user.id)
		localidad = Localidad.objects.filter(id__in=[locality_ids.localidad_id for locality_ids in id_localidad])
		proveedor = Proveedor.objects.filter(localidad__in=[locality.nombre for locality in localidad])
		evento = Evento.objects.filter(proveedor_id__in=[provider.id for provider in proveedor])

		total_claims = Autorizacion.objects.all().filter(tipoAprobacion='1',evento_id__in=[event.id for event in evento]).count()
		falta_claims = Autorizacion.objects.all().filter(estatus__in=['Y','P'],tipoAprobacion='1',evento_id__in=[event.id for event in evento]).count()
		resuelto_claims = total_claims-falta_claims

		emisor = Emisor.objects.filter(rfc__in=[provider.rfc for provider in proveedor])
		comprobantes = Comprobante.objects.filter(emisor_id__in=[trans.id for trans in emisor])

		total_invoices = Autorizacion.objects.all().filter(tipoAprobacion='2',comprobante_id__in=[vouchers.id for vouchers in comprobantes]).count()
		falta_invoices = Autorizacion.objects.all().filter(estatus__in=['Y','P'],tipoAprobacion='2',comprobante_id__in=[vouchers.id for vouchers in comprobantes]).count()
		resuelto_invoices = total_invoices-falta_invoices
	
	return render_to_response('pantallas.html',RequestContext(request,locals()))


@login_required
def usuario_detail(request,id):
	user = info(request)
	user_type = user.type()
	user_name = user.name()
	permission = user.permission(user_type)
	username = get_object_or_404(User,id=id)
	typeUser = get_object_or_404(TipoUsuario,user_id=id)
	localityUser = UsuarioLocalidad.objects.filter(usuario_id=id)
	tipos = TipoUsuario.TIPO_USER
	localidad = Localidad.objects.all()
	if request.POST:
		first_name = request.POST.get("nombre")
		last_name = request.POST.get("apellidos")
		locality = request.POST.get("localidad[]")
		user_type = request.POST.get('tipo')
		email = request.POST.get('correo')
		cellphone = request.POST.get('celular')
		wp = request.POST.get('whatsapp')
		if wp != 'Y':
			wp='N'
		tg = request.POST.get('telegram')
		if tg != 'Y':
			tg='N'
		sms = request.POST.get('sms')
		if sms != 'Y':
			sms='N'
		username = request.POST.get('user')
		password = request.POST.get('pass')
		user = User.objects.filter(id=id).update(username=username, email=email, password=password)
		user.first_name = first_name
		user.last_name = last_name
		if user_type=='S':
			user.is_staff = True
		user.save()
		usertipo = TipoUsuario.objects.filter(usuario_id=id).update(user_id=user.id,tipo=user_type,email=email,celular=cellphone,whatsapp=wp,telegram=tg,sms=sms,tgcontacto='')
		usertipo.save()
		bug = locality
		userlocality = UsuarioLocalidad.objects.filter(usuario_id=id).update(usuario_id=user.id,localidad_id=int(locality))
		userlocality.save()
		message_success = 1
		return render_to_response('settings/registro.html',RequestContext(request,locals()))

	return render_to_response('settings/modificar.html',RequestContext(request,locals()))



@login_required
def list_users(request):
	user = info(request)
	user_type = user.type()
	user_name = user.name()
	permission = user.permission(user_type)
	username = User.objects.all()
	return render_to_response('settings/usuarios.html',RequestContext(request,locals()))

@login_required
def registration(request):
	user = info(request)
	user_type = user.type()
	user_name = user.name()
	permission = user.permission(user_type)
	tipos = TipoUsuario.TIPO_USER
	subTypePmx = TipoUsuario.PEMEX_USER
	subTypeMac = TipoUsuario.MAC_USER
	localidad = Localidad.objects.all()
	typepmx = TipoUsuario.PEMEX
	typemac = TipoUsuario.MAC
	if request.POST:
		first_name = request.POST.get("nombre")
		last_name = request.POST.get("apellidos")
		locality = request.POST.get("local")
		user_type = request.POST.get('tipo')
		user_subtype = request.POST.get('subtipo')
		email = request.POST.get('correo')
		cellphone = request.POST.get('celular')
		wp = request.POST.get('whatsapp')
		if wp != 'Y':
			wp='N'
		tg = request.POST.get('telegram')
		if tg != 'Y':
			tg='N'
		sms = request.POST.get('sms')
		if sms != 'Y':
			sms='N'
		username = request.POST.get('user')
		password = request.POST.get('pass')
		user = User.objects.create_user(username, email, password)
		user.first_name = first_name
		user.last_name = last_name
		if user_type=='S':
			user.is_staff = True
		user.save()
		usertipo = TipoUsuario(user_id=user.id,tipo=user_type,subtipo=user_subtype,email=email,celular=cellphone,whatsapp=wp,telegram=tg,sms=sms,tgcontacto='')
		usertipo.save()
		try:
			localitys = locality.split(",")
			for user_localitys in localitys:
				userlocality = UsuarioLocalidad(usuario_id=user.id,localidad_id=int(user_localitys))
				userlocality.save()
			message_success = 1
			return render_to_response('settings/registro.html',RequestContext(request,locals()))
		except Exception, e:
			userlocality = UsuarioLocalidad(usuario_id=user.id,localidad_id=int(locality))
			userlocality.save()
			message_success = 1
			return render_to_response('settings/registro.html',RequestContext(request,locals()))


	return render_to_response('settings/registro.html',RequestContext(request,locals()))

@login_required
def localitys(request):
	user = info(request)
	user_type = user.type()
	user_name = user.name()
	permission = user.permission(user_type)
	if request.POST:
		code = request.POST.get('codigo')
		locality = request.POST.get('localidad')
		localitys = Localidad(codigo=code,nombre=locality)
		localitys.save()
		message_success = 1
		return render_to_response('settings/localidades.html',RequestContext(request,locals()))


	return render_to_response('settings/localidades.html',RequestContext(request,locals()))


@login_required
def reasons(request):
	user = info(request)
	user_type = user.type()
	user_name = user.name()
	permission = user.permission(user_type)
	motivos = Motivos.objects.all()
	return render_to_response('settings/motivos.html',RequestContext(request,locals()))


def erace(request):
	return




def permisos(request):
	user = info(request)
	user_type = user.type()
	user_name = user.name()
	permission = user.permission(user_type)
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

def save_ligar(request):
    if request.method == 'POST':
        evento = int(request.POST.get('evento'))
        comprobante = int(request.POST.get('comprobante'))
        CE = ComprobanteEvento.objects.filter(evento=evento, comprobante=comprobante)
        Almacenar = True
        for EventVoucher in CE:
        	EventVoucher.delete()
        	Almacenar = False
        if Almacenar:
        	liga = ComprobanteEvento(evento=evento, comprobante=comprobante)
        	liga.save()
        response_data = {}
        response_data['result'] = 'Create post successful!'
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

def save_level(request):
    if request.method == 'POST':
    	x = datetime.datetime.now()
    	if x.month < 10:
    		fecha = "%s-0%s-%s"% (x.year, x.month, x.day)
    	else:
    		fecha = "%s-%s-%s"% (x.year, x.month, x.day)
    	comprobante = int(request.POST.get('comprobante'))
        tipo = request.POST.get('tipo')

        level = ComprobanteTipo(tipo=tipo,fecha=fecha,usuario=request.user.id,comprobante=comprobante)
        level.save()
        response_data = {}
        response_data['result'] = 'Create post successful!'
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

