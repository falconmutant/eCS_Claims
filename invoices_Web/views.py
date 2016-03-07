from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from invoices_Web.models import *
from .utils import Methods
from settings.utils import info
from claims.models import TipoUsuario

invoice = Methods()
message_success=0
message_error=0

@login_required
def invoices(request):
	try:
		user = info(request)
		user_type = user.type()
		user_name = user.name()
		start,end = user.date()
		permission = user.permission(user_type,user.subType())
		success = message_success
		error = message_error
		global message_success
		message_success = 0
		global message_error
		message_error = 0
		if user.type() == TipoUsuario.MAC or user.type() == TipoUsuario.PEMEX:
			locality = invoice.get_locality_user(user.id())
			provider = invoice.get_providers_locality(locality)
			company = invoice.get_company_provider(provider)
			voucher = invoice.get_voucher_company(company)
			typeVoucher = invoice.get_typeVoucher_voucher(voucher)
			auth = invoice.get_auth_type(user.type(),user.subType(),'invoice',voucher)
		elif user.type() == TipoUsuario.ECARESOFT or user.type() == TipoUsuario.SUPERUSER:
			auth = invoice.get_auth_type(user.type(),'','history','')
			voucher = invoice.get_voucher_auth(auth)
			company = invoice.get_company_voucher(voucher)
			typeVoucher = invoice.get_typeVoucher_voucher(voucher)
		if request.POST:
			invoice.set_date(request.POST.get("daterange").split(" - ")[0],request.POST.get("daterange").split(" - ")[1])
			auth = invoice.get_auth_filter(auth,'date','')
			start,end = invoice.get_date()
		return render_to_response('invoices/invoices.html',RequestContext(request,locals()))
	except Exception, e:
		bug = e
		return render_to_response('404.html',RequestContext(request,locals()))

@login_required
def detalle(request, id):
	try:
		user = info(request)
		user_type = user.type()
		user_name = user.name()
		permission = user.permission(user_type,user.subType())
		detail = invoice.get_voucher_object(id)
		concept = invoice.get_concepts_voucher(id)
		company = invoice.get_company_voucher(id)
		provider = invoice.get_provider_company(company.rfc)
		eventVoucher = invoice.get_eventVoucher_voucher(id)
		event = invoice.get_event_provider_exclude(provider.id,eventVoucher)
		patient = invoice.get_patient_event(event)
		tax = invoice.get_tax_voucher(id)
		allevent = invoice.get_event_provider(provider.id)
		cause = invoice.get_cause()
		auth = invoice.get_auth_user(user.type())

		if request.POST:
			status = request.POST.get('estatus')
			description = request.POST.get('descripcion')
			cause = request.POST.get('motivo')
			invoice.set_auth_status(id,status,description,cause)
			global message_success
			message_success = 1
			global message_error
			message_error = 1
			return HttpResponseRedirect('/invoice/')
				
		return render_to_response('invoices/detalles.html',RequestContext(request,locals()))
	except Exception, e:
		bug = e
		return render_to_response('404.html',RequestContext(request,locals()))

@login_required
def historial(request):
	try:
		user = info(request)
		user_type = user.type()
		user_name = user.name()
		permission = user.permission(user_type,user.subType())
		if user.type() == TipoUsuario.MAC or user.type() == TipoUsuario.PEMEX:
			locality = invoice.get_locality_user(user.id())
			provider = invoice.get_providers_locality(locality)
			company = invoice.get_company_provider(provider)
			voucher = invoice.get_voucher_company(company)
			typeVoucher = invoice.get_typeVoucher_voucher(voucher)
			auth = invoice.get_auth_type(user.type(),user.subType(),'history',voucher)
		elif user.type() == TipoUsuario.ECARESOFT or user.type() == TipoUsuario.SUPERUSER:
			auth = invoice.get_auth_type(user.type(),'','history','')
			voucher = invoice.get_voucher_auth(auth)
			company = invoice.get_company_voucher(voucher)
			typeVoucher = invoice.get_typeVoucher_voucher(voucher)
		return render_to_response('invoices/historial.html',RequestContext(request,locals()))
	except Exception, e:
		bug = e
		return render_to_response('404.html',RequestContext(request,locals()))