from claims.models import *
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib import auth
import httplib2 as http
import json
from settings.external import *
try:
	from urlparse import urlparse
except ImportError:
	from urllib.parse import urlparse

class Method:

	def get_locality_user(self,userid):
		locality = {}
		localityid = UsuarioLocalidad.objects.filter(usuario_id=userid)
		locality = Localidad.objects.filter(id__in=[locality_ids.localidad_id for locality_ids in localityid])
		return locality

	def get_providers_locality(self,locality):
		return Proveedor.objects.filter(localidad__in=[localitys.nombre for localitys in locality])

	def get_event_provider(self,provider):
		return Evento.objects.filter(proveedor_id__in=[providers.id for providers in provider])

	def get_patient_event(self,event):
		try:
			return Paciente.objects.filter(evento_id__in=[events.id for events in event])
		except Exception, e:
			return get_object_or_404(Paciente,evento_id=event)

	def get_process_event(self,eventid):
		return Procedimiento.objects.filter(evento_id__in=[event.id for event in eventid])

	def get_auth_type(self,usertype,eventype,event):
		auth={}
		if usertype == TipoUsuario.MAC:
			if eventype == 'history':
				auth = Autorizacion.objects.all().filter(estatus__in=['A','X','Y','N','P'],tipoAprobacion='1',evento_id__in=[events.id for events in event])
			else:
				auth = Autorizacion.objects.filter(estatus__in=['E','R'],tipoAprobacion='1',evento_id__in=[events.id for events in event])
		elif usertype == TipoUsuario.PEMEX:
			if eventype == 'history':
				auth = Autorizacion.objects.all().filter(estatus__in=['X'],tipoAprobacion='1',evento_id__in=[events.id for events in event])
			else:
				auth = Autorizacion.objects.filter(estatus__in=['Y','P'],tipoAprobacion='1',evento_id__in=[events.id for events in event])
		elif usertype == TipoUsuario.ECARESOFT:
			auth = Autorizacion.objects.filter(estatus__in=['E','R','A','P'],tipoAprobacion='1')
		elif usertype == TipoUsuario.SUPERUSER:
			auth = Autorizacion.objects.filter(estatus__in=['E','R','A','P'],tipoAprobacion='1')
		return auth

	def get_auth_filter(self,auth,value,obj):
		if value == 'date':
			auth = auth.filter(fechaSolicitud__range=[self.start, self.end])
		if value == 'status':
			auth = auth.filter(estatus__in=obj)
		if value == 'type':
			auth = auth.filter(tipoAprobacion=obj)
		return auth

	def get_event_auth(self,auth):
		return Evento.objects.filter(id__in= [auths.evento_id for auths in auth])

	def get_choice_auth(self,typeUser):
		AUTH_ESTATUS_TEMPLATE=()
		if typeUser == TipoUsuario.MAC:
			AUTH_ESTATUS_TEMPLATE =(
				('Y', 'Aceptado'),
				('N', 'Rechazado'),
				('E', 'En Revision'),
			)
		elif typeUser == TipoUsuario.PEMEX:
			AUTH_ESTATUS_TEMPLATE =(
				('A', 'Aceptado'),
				('X', 'Rechazado'),
				('P', 'En Revision'),
			)
		return AUTH_ESTATUS_TEMPLATE

	def get_attachment(self,patientCurp,idCumulus):
		headers = {
		    'Content-Type': 'application/json; charset=UTF-8',
		    'Authorization': 'Token bdc83da3790dc45f272344255e079edff0b4ca60'
		}

		uri = Cumulus
		path = '/pacientes/'+patientCurp+'/eventos/'+str(idCumulus)

		target = urlparse(uri+path)
		method = 'GET'
		body = ''

		h = http.Http()
		# If you need authentication some example:

		response, content = h.request(
		        target.geturl(),
		        method,
		        body,
		        headers)

		# assume that content is a json reply
		# parse content with the json module
		return json.loads(content)

	def get_provider_event(self,event):
		return Proveedor.objects.filter(id__in=[events.proveedor_id for events in event])

	def get_locality_provider(self,provider):
		return Localidad.objects.filter(nombre__in=[providers.localidad for providers in provider])

	def get_date(self):
		return self.start,self.end

	def get_event_object(self,eventid):
		event = get_object_or_404(Evento,id=eventid)
		return event

	def get_dx_event(self,eventid):
		try:
			dx = Dx.objects.filter(evento_id__in=[event.id for event in eventid])
		except Exception, e:
			dx = Dx.objects.filter(evento_id=eventid)
		return dx

	def get_charge_event(self,eventid):
		try:
			charge = Cargo.objects.filter(evento_id__in=[event.id for event in eventid])
		except Exception, e:
			charge = Cargo.objects.filter(evento_id=eventid)
		return charge

	def get_provider_object(self,providerid):
		provider = get_object_or_404(Proveedor,id=providerid)
		return provider

	def get_medic_event(self,event):
		try:
			medic = Medico.objects.filter(evento_id__in=[events.id for events in event])
		except Exception, e:
			medic = Medico.objects.filter(evento_id=event)
		return medic

	def get_cause(self):
		return Motivos.objects.all()

	def get_process_event_medic(self,eventid,medicid):
		process = {}
		try:
			process = Procedimiento.objects.filter(evento_id__in=[event.id for event in eventid],medico_id__in=[medic.id for medic in medicid])
		except Exception, e:
			process = Procedimiento.objects.filter(evento_id=eventid,medico_id__in=[medic.id for medic in medicid])
		return process
	
	def set_date(self,start,end):
		self.start = start
		self.end = end

	def set_userid(self,id):
		self.id = id

	def filters(self,queryset,field,objects):
		queryset = queryset.filter(field=objects)
		return queryset

	def set_auth_status(self,id,status,comment,cause):
		Autorizacion.objects.filter(evento_id=id).update(estatus=status,comentarios=comment,motivo_id=cause)


#try:
#			if estatus == 'Y':
#				detalle = get_object_or_404(Evento, id=id)
#				locality = UsuarioLocalidad.objects.filter(usuario = request.user.id)
#				for localitys in locality:
#					message = 'Se ha Autorizado el Estado de Cuenta {0}, por el sectorial MAC. Favor de revisar Sistema'.format(detalle.folioAut)
#					sendNotifications(localitys.localidad,message, TipoUsuario.PEMEX)
#			if estatus == 'A':
#				detalle = get_object_or_404(Evento, id=id)
#				locality = UsuarioLocalidad.objects.filter(usuario = request.user.id)
#				for localitys in locality:
#					message = 'Se ha Autorizado el Estado de Cuenta {0}, por el sectorial PEMEX.'.format(detalle.folioAut)
#					sendNotifications(localitys.localidad,message, TipoUsuario.MAC)
#		except Exception, e:
#			message_error = 1










