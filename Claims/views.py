from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from Claims.models import *

@login_required
def logged_in(request):
    return render_to_response('pantallas.html',
        context_instance=RequestContext(request)
    )

def detalle(request):
    return render_to_response('detalles.html',
        context_instance=RequestContext(request)
    )

def claims(request):
	eventos = Evento.objects.all()
    return render_to_response('claims.html',RequestContext(request,locals()))

