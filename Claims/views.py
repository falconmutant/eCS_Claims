from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from Claims.models import *

def index(request):
    return render_to_response('index.html',
        context_instance=RequestContext(request)
    )


@login_required
def logged_in(request):
    return render_to_response('pantallas.html',
        context_instance=RequestContext(request)
    )

def detalle(request, id):
	detalle = get_object_or_404(Evento, id=id)
    	return render_to_response('detalles.html',
        	context_instance=RequestContext(request,locals())
    	)

def claims(request):
	autorizacion = Autorizaciones.objects.all()
	evento = Evento.objects.all()
	paciente = Paciente.objects.all()
	medico = Medico.objects.all()
	proveedor = Proveedor.objects.all()
	tipo = TipoServicio.objects.all()
	cargo = CargoPorEvento.objects.all()
	costo = Cargo.objects.all()
    	return render_to_response('claims.html',RequestContext(request,locals()))