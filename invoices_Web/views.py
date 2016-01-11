from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from invoices_Web.models import *
from claims.models import *
import datetime
from django.db.models import Count

@login_required
def detalle(request, id):
	idd=id
	bandera=0
	if request.POST:
		estatus = request.POST.get('estatus')
		descripcion = request.POST.get('descripcion')
		Autorizacion.objects.filter(evento_id=idd).update(Estatus=estatus,Comentarios=descripcion)
		bandera=1
		nombre = request.user.get_full_name()
		autorizacion = Autorizacion.objects.all().filter(Estatus='R',TipoAprobacion='2')
		evento = Evento.objects.all()
		paciente = Paciente.objects.all()
		proveedor = Proveedor.objects.all()
		cargo = Cargos.objects.all()
		return render_to_response('claims/claims.html',RequestContext(request,locals()))
	nombre = request.user.get_full_name()

	detalle = get_object_or_404(Comprobante, id=id)
	conceptos = Conceptos.objects.all()
	emisor = get_object_or_404(Emisor, id=detalle.emisor_id)
	proveedor = get_object_or_404(Proveedor, rfc=emisor.rfc)
	evento = Evento.objects.filter(proveedor_id=proveedor.id)
	paciente =  Paciente.objects.all()
	autorizacion = Autorizacion.objects.filter(Estatus="R")
	return render_to_response('invoices/detalles.html',RequestContext(request,locals()))

def save_ligar(request):
    if request.method == 'POST':
        evento = request.POST.get('evento')
        comprobante = request.POST.get('comprobante')
        liga = ComprobanteEvento(comprobante=comprobante, evento=evento)
        response_data = {}
        response_data['result'] = 'Create post successful!'
        liga.save()
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
	inicio = "%s-%s-%s"% (x.year, x.month, x.day)
	fin = "%s-%s-%s"% (x.year, x.month, x.day)
	nombre = request.user.get_full_name()

	comprobante = Comprobante.objects.all()
	cliente = Emisor.objects.all()
	conceptos = Conceptos.objects.all()
	servicios = Conceptos.objects.annotate(number_of_concepts=Count('comprobante_id'))



	if request.POST:
		autorizacion = Autorizacion.objects.all().filter(Estatus='R',TipoAprobacion='2',FechaSolicitud__range=[request.POST.get("inicio"), request.POST.get("fin")])
		if request.POST.get("tipo") != 'vacio':
			autorizacion = Autorizacion.objects.all().filter(Sistema=request.POST.get("tipo"),TipoAprobacion='2')
		if request.POST.get("cliente") != 'vacio':
			Autorizacion = Autorizacion.objects.all().filter(cliente_id=request.POST.get("cliente"))
		inicio = request.POST.get("inicio")
		fin = request.POST.get("fin")

    	return render_to_response('invoices/invoices.html',RequestContext(request,locals()))

@login_required
def historial(request):
	nombre = request.user.get_full_name()
	x = datetime.datetime.now()
	inicio = "%s-%s-%s"% (x.year, x.month, x.day)
	fin = "%s-%s-%s"% (x.year, x.month, x.day)
	nombre = request.user.get_full_name()

	comprobante = Comprobante.objects.all()
	cliente = Emisor.objects.all()
	conceptos = Conceptos.objects.all()
	servicios = Conceptos.objects.annotate(number_of_concepts=Count('comprobante_id'))
    	return render_to_response('invoices/historial.html',RequestContext(request,locals()))