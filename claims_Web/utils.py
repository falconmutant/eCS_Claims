from claims.models import *
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib import auth


class Methods:
	def get_info_user(self,request):
		id = request.user.id
		name = request.user.get_full_name()
		type = get_object_or_404(TipoUsuario,user_id=user.id)
		return id,name,type

	def get_cause():
		cause = Motivos.objects.all()
		return cause

	def get_cause_object(causeid):
		cause = get_object_or_404(Motivos,id=causeid)
		return cause

	def get_locality_user(userid):
		localityid = UsuarioLocalidad.objects.filter(usuario_id=userid)
		locality = Localidad.objects.filter(id__in=[locality_ids.localidad_id for locality_ids in localityid])
		return locality

	def get_locality_object(localityid):
		locality = get_object_or_404(Localidad,id=localityid)
		return locality

	def get_localitys():
		localitys = Localidad.objects.all()
		return localitys

	def get_providers_locality(locality):
		provider = Proveedor.objects.filter(localidad__in=[localitys.nombre for localitys in locality])
		return provider

	def get_provider_rfc(providerrfc):
		provider = get_object_or_404(Proveedor,rfc=providerrfc)
		return provider

	def get_provider_object(providerid):
		provider = get_object_or_404(Proveedor,rfc=providerid)
		return provider

	def get_providers():
		providers = Proveedor.objects.all()
		return providers

	def get_event_provider(provider):
		event = Evento.objects.filter(proveedor_id__in=[providers.id for providers in provider])
		return event

	def get_event_object(eventid):
		event = get_object_or_404(Evento,id=eventid)
		return event

	def get_events():
		events = Evento.objects.all()
		return events

	def get_patients():
		patients = Paciente.objects.all()
		return patients

	def get_patient_object(patientid):
		patient = get_object_or_404(Paciente,id=patientid)
		return patient

	def get_patient_event(event):
		patient = Paciente.objects.filter(evento_id__in=[events.id for events in event])
		return patient

	def get_medics():
		medics = Medico.objects.all()
		return medics

	def get_medic_object(medicid):
		medic = get_object_or_404(Medico,id=medicid)
		return medic

	def get_medic_event(event):
		medic = Medico.objects.filter(evento_id__in=[events.id for events in event])
		return medic

	def get_process_medic(medicid):
		process = Procedimiento.objects.filter(medico_id__in=[medic.id for medic in medicid])
		return process

	def get_process_event(eventid):
		process = Procedimiento.objects.filter(evento_id__in=[event.id for event in eventid])
		return process

	def get_process_object(processid):
		process = get_object_or_404(Procedimiento,id=processid)
		return process

	def get_dx_medic(medicid):
		dx = Dx.objects.filter(medico_id__in=[medic.id for medic in medicid])
		return dx

	def get_dx_event(eventid):
		dx = Dx.objects.filter(evento_id__in=[event.id for event in eventid])
		return dx

	def get_dx_object(dxid):
		dx = get_object_or_404(Dx,id=dxid)
		return dx

	def get_charge_event(eventid):
		charge = Cargo.objects.filter(evento_id__in=[event.id for event in eventid])
		return charge

	def get_charge_object(chargeid):
		charge = get_object_or_404(Cargo,id=chargeid)
		return charge

	def get_auth_type(type):
		if self.type == TipoUsuario.MAC:
			auth = Autorizacion.objects.filter(Estatus__in=['E','R'],TipoAprobacion='1')
		if self.type == TipoUsuario.PEMEX:
			auth = Autorizacion.objects.filter(Estatus__in=['Y','P'],TipoAprobacion='1')
		if self.type == TipoUsuario.ECARESOFT:
			auth = Autorizacion.objects.filter(Estatus__in=['E','R','A','P'],TipoAprobacion='1')
		if self.type == TipoUsuario.SUPERUSER:
			auth = Autorizacion.objects.filter(Estatus__in=['E','R','A','P'],TipoAprobacion='1')
		return auth

	def get_auth_filter(auth,filter,obj):
		if self.filter == 'event':
			auth = auth.filter(evento_id__in=[event.id for event in obj]);
		if self.filter == 'date':
			auth = auth.filter(FechaSolicitud__range=[obj.start, obj.end]);
		return auth
















