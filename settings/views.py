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

# Create your views here.
@login_required
def registration(request):
	nombre_user = request.user.get_full_name()
	tipos = TipoUsuario.TIPO_USER
	localidad = Localidad.objects.all()
	if request.POST:
		first_name = request.POST.get("nombre")
		last_name = request.POST.get("apellidos")
		locality = request.POST.get("localidad")
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
		user = User.objects.create_user(username, email, password)
		user.first_name = first_name
		user.last_name = last_name
		if user_type=='S':
			user.is_staff = True
		user.save()
		usertipo = TipoUsuario(user_id=user.id,tipo=user_type,email=email,celular=cellphone,whatsapp=wp,telegram=tg,sms=sms,tgcontacto='')
		usertipo.save()
		for localitys in locality:
			userlocality = UsuarioLocalidad(usuario_id=user.id,localidad_id=int(localitys))
			userlocality.save()
		message_success = 1
		return render_to_response('settings/registro.html',RequestContext(request,locals()))


	return render_to_response('settings/registro.html',RequestContext(request,locals()))

@login_required
def localitys(request):
	nombre_user = request.user.get_full_name()
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
	nombre_user = request.user.get_full_name()
	motivos = Motivos.objects.all()
	return render_to_response('settings/motivos.html',RequestContext(request,locals()))


def erace(request):
	return

