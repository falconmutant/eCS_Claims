import json
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from invoices_Web.models import *
from django.contrib import auth
from claims.models import *
import datetime
from django.db.models import Count

@login_required
def detalle(request, id):
	nombre_user = request.user.get_full_name()
	tipouser = get_object_or_404(TipoUsuario,user_id=request.user.id)
	if request.POST:
		estatus = request.POST.get('estatus')
		descripcion = request.POST.get('descripcion')
		Autorizacion.objects.filter(comprobante_id=id).update(estatus=estatus,Comentarios=descripcion)
		return HttpResponseRedirect('/invoice/')
	
	try:
		detalle = get_object_or_404(Comprobante, id=id)
		conceptos = Conceptos.objects.filter(comprobante_id=detalle.id)
		emisor = get_object_or_404(Emisor, id=detalle.emisor_id)
		proveedor = get_object_or_404(Proveedor, rfc=emisor.rfc)
		CE = ComprobanteEvento.objects.all().filter(comprobante=id)
		evento = Evento.objects.filter(proveedor_id=proveedor.id).exclude(id__in=[CompEvent.evento for CompEvent in CE])
		paciente =  Paciente.objects.all().filter(evento_id__in=[event2.id for event2 in evento])
		tax = get_object_or_404(Impuesto,comprobante_id=detalle.id)
		fullevento = Evento.objects.filter(proveedor_id=proveedor.id)
		motivo = Motivos.objects.all()
		if tipouser.tipo == TipoUsuario.MAC:
			autorizacion = Autorizacion.objects.all().filter(estatus__in='A',tipoAprobacion='1')
		if tipouser.tipo == TipoUsuario.PEMEX:
			autorizacion = Autorizacion.objects.all().filter(estatus__in='Y',tipoAprobacion='1')		

		return render_to_response('invoices/detalles.html',RequestContext(request,locals()))
	except Exception, e:
		bugerror = e
		return render_to_response('invoices/detalles.html',RequestContext(request,locals()))

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




@login_required
def invoices(request):
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
	emisor = Emisor.objects.filter(rfc__in=[provider.rfc for provider in proveedor])
	comprobante = Comprobante.objects.filter(emisor_id__in=[trans.id for trans in emisor])
	cliente = Emisor.objects.filter(id__in=[invoice.emisor_id for invoice in comprobante])
	comptipo = ComprobanteTipo.objects.filter(comprobante__in=[comp.id for comp in comprobante])

	if tipouser.tipo == TipoUsuario.MAC:
		autorizacion = Autorizacion.objects.all().filter(estatus__in=['E','R'],tipoAprobacion='2',comprobante_id__in=[vouchers.id for vouchers in comprobante])
	if tipouser.tipo == TipoUsuario.PEMEX:
		autorizacion = Autorizacion.objects.all().filter(estatus__in=['Y','P'],tipoAprobacion='2',comprobante_id__in=[vouchers.id for vouchers in comprobante])
	if tipouser.tipo == TipoUsuario.ECARESOFT:
		autorizacion = Autorizacion.objects.all().filter(estatus__in=['E','R','A','P'],tipoAprobacion='2')
	if tipouser.tipo == TipoUsuario.SUPERUSER:
		autorizacion = Autorizacion.objects.all().filter(estatus__in=['E','R','A','P'],tipoAprobacion='2')

	if request.POST:
		inicio = request.POST.get("daterange").split(" - ")[0]
		fin = request.POST.get("daterange").split(" - ")[1]
		if tipouser.tipo == TipoUsuario.MAC:
			autorizacion = autorizacion.filter(fechaSolicitud__range=[inicio, fin])
		if tipouser.tipo == TipoUsuario.PEMEX:
			autorizacion = autorizacion.filter(fechaSolicitud__range=[inicio, fin])
		if tipouser.tipo == TipoUsuario.ECARESOFT:
			autorizacion = autorizacion.filter(fechaSolicitud__range=[inicio, fin])
		if tipouser.tipo == TipoUsuario.SUPERUSER:
			autorizacion = autorizacion.filter(fechaSolicitud__range=[inicio, fin])	
    	return render_to_response('invoices/invoices.html',RequestContext(request,locals()))

@login_required
def historial(request):
	nombre_user = request.user.get_full_name()
	tipouser = get_object_or_404(TipoUsuario,user_id=request.user.id)

	id_localidad = UsuarioLocalidad.objects.filter(usuario_id=request.user.id)
	localidad = Localidad.objects.filter(id__in=[locality_ids.localidad_id for locality_ids in id_localidad])
	proveedor = Proveedor.objects.filter(localidad__in=[locality.nombre for locality in localidad])
	emisor = Emisor.objects.filter(rfc__in=[provider.rfc for provider in proveedor])
	comprobante = Comprobante.objects.filter(emisor_id__in=[trans.id for trans in emisor])
	cliente = Emisor.objects.filter(id__in=[invoice.emisor_id for invoice in comprobante])
	comptipo = ComprobanteTipo.objects.filter(comprobante__in=[comp.id for comp in comprobante])

	if tipouser.tipo == TipoUsuario.MAC:
		autorizacion = Autorizacion.objects.all().filter(estatus__in=['A','X','Y','N','P'],tipoAprobacion='2',comprobante_id__in=[vouchers.id for vouchers in comprobante])
	if tipouser.tipo == TipoUsuario.PEMEX:
		autorizacion = Autorizacion.objects.all().filter(estatus__in=['X'],tipoAprobacion='2',comprobante_id__in=[vouchers.id for vouchers in comprobante])
	if tipouser.tipo == TipoUsuario.ECARESOFT:
		autorizacion = Autorizacion.objects.all().filter(tipoAprobacion='2',)
	if tipouser.tipo == TipoUsuario.SUPERUSER:
		autorizacion = Autorizacion.objects.all().filter(tipoAprobacion='2')

	return render_to_response('invoices/historial.html',RequestContext(request,locals()))
