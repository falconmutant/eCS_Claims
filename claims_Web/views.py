import json
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib import auth
from .utils import Method
from settings.utils import info
from claims.models import TipoUsuario

claim = Method()
message_success=0
message_error=0

@login_required
def claims(request):
	user = info(request)
	user_type = user.type()
	user_name = user.name()
	start,end = user.date()
	permission = user.permission(user_type)
	success = message_success
	error = message_error
	global message_success
	message_success = 0
	global message_error
	message_error = 0

	try:
		if user.type() == TipoUsuario.MAC or user.type() == TipoUsuario.PEMEX:
			locality = claim.get_locality_user(user.id())
			provider= claim.get_providers_locality(locality)
			event = claim.get_event_provider(provider)
			patient = claim.get_patient_event(event)
			auth = claim.get_auth_type(user.type(),'claims',event)

		elif user.type() == TipoUsuario.ECARESOFT or user.type() == TipoUsuario.SUPERUSER:
			auth = claim.get_auth_type(user.type(),'claims','')
			event = claim.get_event_auth(auth)
			patient = claim.get_patient_event(event)
			provider = claim.get_provider_event(event)
			locality = claim.get_locality_provider(provider)

		if request.POST:
			claim.set_date(request.POST.get("daterange").split(" - ")[0],request.POST.get("daterange").split(" - ")[1])
			auth = claim.get_auth_filter(auth,'date','')
			start,end = claim.get_date()

		return render_to_response('claims/claims.html',RequestContext(request,locals()))
	except Exception, e:
		bug = e
		return render_to_response('404.html',RequestContext(request,locals()))

@login_required
def detalle(request, id):
	user = info(request)
	user_type = user.type()
	user_name = user.name()
	permission = user.permission(user_type)
	try:
		detail = claim.get_event_object(id)
		patient = claim.get_patient_event(id)
		dx = claim.get_dx_event(id)
		charge = claim.get_charge_event(id)
		provider = claim.get_provider_object(detail.proveedor_id)
		medic = claim.get_medic_event(id)
		cause = claim.get_cause()
		procedure = claim.get_process_event_medic(id,medic)
		auth_type = claim.get_choice_auth(user.type())
		if request.POST:
			status = request.POST.get('estatus')
			description = request.POST.get('descripcion')
			cause = request.POST.get('motivo')
			claim.set_auth_status(id,status,description,cause)
			global message_success
			message_success = 1
			global message_error
			message_error = 1
			return HttpResponseRedirect('/claims/')
		return render_to_response('claims/detalles.html',RequestContext(request,locals()))
	except Exception, e:
		bug = e
		return render_to_response('404.html',RequestContext(request,locals()))

@login_required
def historial(request):
	user = info(request)
	user_type = user.type()
	user_name = user.name()
	permission = user.permission(user_type)
	try:
		if user.type() == TipoUsuario.MAC or user.type() == TipoUsuario.PEMEX:
			locality = claim.get_locality_user(user.id())
			provider= claim.get_providers_locality(locality)
			event = claim.get_event_provider(provider)
			patient = claim.get_patient_event(event)
			charge = claim.get_process_event(event)
			auth = claim.get_auth_type(user.type(),'history',event)
		elif user.type() == TipoUsuario.ECARESOFT or user.type() == TipoUsuario.SUPERUSER:
			auth = claim.get_auth_type(user.type(),'history','')
			event = claim.get_event_auth(auth)
			patient = claim.get_patient_event(event)
			provider = claim.get_provider_event(event)
			locality = claim.get_locality_provider(provider)
		return render_to_response('claims/historial.html',RequestContext(request,locals()))
	except Exception, e:
		bug = e
		return render_to_response('404.html',RequestContext(request,locals()))

@login_required
def detalle_historial(request, id):
	user = info(request)
	user_type = user.type()
	user_name = user.name()
	permission = user.permission(user_type)
	try:
		detail = claim.get_event_object(id)
		patient = claim.get_patient_event(id)
		dx = claim.get_dx_event(id)
		charge = claim.get_charge_event(id)
		provider = claim.get_provider_object(detail.proveedor_id)
		medic = claim.get_medic_event(id)
		cause = claim.get_cause()
		procedure = claim.get_process_event_medic(id,medic)
		auth_type = claim.get_choice_auth(user.type())
		return render_to_response('claims/historial_detalles.html',RequestContext(request,locals()))
	except Exception, e:
		bug = e
		return render_to_response('404.html',RequestContext(request,locals()))