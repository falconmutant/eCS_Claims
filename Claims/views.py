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
		Autorizaciones.objects.filter(id=idd).update(Estatus=estatus,Comentarios=descripcion)
		bandera=1
		nombre = request.user.get_full_name()
		autorizacion = Autorizaciones.objects.all().filter(Estatus='Recibido')
		evento = Evento.objects.all()
		paciente = Paciente.objects.all()
		proveedor = Proveedor.objects.all()
		cargo = CargoPorEvento.objects.all()
		costo = Cargo.objects.all()
		return render_to_response('claims.html',RequestContext(request,locals()))
	nombre = request.user.get_full_name()
	detalle = get_object_or_404(Evento, id=id)
	paciente = Paciente.objects.all()
	medico = Medico.objects.all()
	cargo = CargoPorEvento.objects.all()
	costo = Cargo.objects.all()
	tipocargo = TipoCargo.objects.all()
	return render_to_response('detalles.html',RequestContext(request,locals()))

@login_required
def claims(request):
	x = datetime.datetime.now()
	inicio = "%s-%s-%s"% (x.year, x.month, x.day)
	fin = "%s-%s-%s"% (x.year, x.month, x.day)
	nombre = request.user.get_full_name()
	autorizacion = Autorizaciones.objects.all().filter(Estatus='Recibido')
	evento = Evento.objects.all()
	paciente = Paciente.objects.all()
	proveedor = Proveedor.objects.all()
	cargo = CargoPorEvento.objects.all()
	costo = Cargo.objects.all()
	if request.POST:
		if request.POST.get("tipo") != 'vacio':
			evento = Evento.objects.all().filter(IdTipoServicio_id=request.POST.get("tipo"))
		if request.POST.get("cliente") != 'vacio':
			proveedor = Proveedor.objects.all().filter(Proveedor=request.POST.get("cliente"))
		autorizacion = Autorizaciones.objects.all().filter(Estatus='Recibido',
															FechaSolicitud > request.POST.get("inicio"),
															FechaSolicitud < request.POST.get("fin"))
		inicio = request.POST.get("inicio")
		fin = request.POST.get("fin")
    	return render_to_response('claims.html',RequestContext(request,locals()))

@login_required
def historial(request):
	nombre = request.user.get_full_name()
	autorizacion = Autorizaciones.objects.all()
	evento = Evento.objects.all()
	paciente = Paciente.objects.all()
	proveedor = Proveedor.objects.all()
	cargo = CargoPorEvento.objects.all()
	costo = Cargo.objects.all()
    	return render_to_response('historial.html',RequestContext(request,locals()))