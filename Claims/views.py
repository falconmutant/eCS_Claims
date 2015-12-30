from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from Claims.models import *
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
		Autorizacion.objects.filter(id=idd).update(Estatus=estatus,Comentarios=descripcion)
		bandera=1
		nombre = request.user.get_full_name()
		autorizacion = Autorizacion.objects.all().filter(Estatus='Recibido')
		cuenta = Cuenta.objects.all()
		paciente = Paciente.objects.all()
		proveedor = Proveedor.objects.all()
		Cargo = Cargo.objects.all()
		return render_to_response('claims/claims.html',RequestContext(request,locals()))
	nombre = request.user.get_full_name()
	detalle = get_object_or_404(Cuenta, id=id)
	paciente = Paciente.objects.all()
	medico = Medico.objects.all()
	cargo = Cargo.objects.all()
	return render_to_response('claims/detalles.html',RequestContext(request,locals()))

@login_required
def claims(request):
	x = datetime.datetime.now()
	inicio = "%s-%s-%s"% (x.year, x.month, x.day)
	fin = "%s-%s-%s"% (x.year, x.month, x.day)
	nombre = request.user.get_full_name()
	autorizacion = Autorizacion.objects.all().filter(Estatus='Recibido',TipoAprobacion='1')
	cuenta = Cuenta.objects.all()
	paciente = Paciente.objects.all()
	proveedor = Proveedor.objects.all()
	cargo = Cargo.objects.all()
	if request.POST:
		autorizacion = Autorizacion.objects.all().filter(Estatus='Recibido',FechaSolicitud__range=[request.POST.get("inicio"), request.POST.get("fin")])
		if request.POST.get("tipo") != 'vacio':
			autorizacion = Autorizacion.objects.all().filter(Sistema=request.POST.get("tipo"))
		if request.POST.get("cliente") != 'vacio':
			cuenta = Cuenta.objects.all().filter(IdProveedor_id=request.POST.get("cliente"))
		inicio = request.POST.get("inicio")
		fin = request.POST.get("fin")

    	return render_to_response('claims/claims.html',RequestContext(request,locals()))

@login_required
def historial(request):
	nombre = request.user.get_full_name()
	autorizacion = Autorizacion.objects.all()
	evento = Cuenta.objects.all()
	paciente = Paciente.objects.all()
	proveedor = Proveedor.objects.all()
	cargo = Cargo.objects.all()
    	return render_to_response('claims/historial.html',RequestContext(request,locals()))