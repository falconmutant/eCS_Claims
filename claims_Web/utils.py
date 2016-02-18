from claims.models import *
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib import auth
import datetime

class info:
	def __init__(self,request):
		self.request = request

	def id(self):
		return self.request.user.id

	def name(self):
		return self.request.user.get_full_name()

	def type(self):
		return get_object_or_404(TipoUsuario,user_id=self.request.user.id).tipo
	
	def date(self):
		datenow = datetime.datetime.now()
		if x.month < 10:
			self.start = "%s-0%s-%s"% (x.year, x.month, x.day)
			self.end = "%s-0%s-%s"% (x.year, x.month, x.day)
		else:
			self.start = "%s-%s-%s"% (x.year, x.month, x.day)
			self.end = "%s-%s-%s"% (x.year, x.month, x.day)
		return self.start,self.end



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















	def get_cause(self):
		return Motivos.objects.all()

	

	def get_locality_object(self,localityid):
		locality = get_object_or_404(Localidad,id=localityid)
		return locality

	def get_localitys(self):
		localitys = Localidad.objects.all()
		return localitys

	

	def get_provider_rfc(self,providerrfc):
		provider = get_object_or_404(Proveedor,rfc=providerrfc)
		return provider

	def get_provider_object(self,providerid):
		provider = get_object_or_404(Proveedor,id=providerid)
		return provider

	def get_providers(self):
		providers = {}
		providers = Proveedor.objects.all()
		return providers

	

	def get_event_object(self,eventid):
		event = get_object_or_404(Evento,id=eventid)
		return event

	

	def get_patients(self):
		patients = {}
		patients = Paciente.objects.all()
		return patients

	def get_patient_object(self,patientid):
		patient = get_object_or_404(Paciente,id=patientid)
		return patient

	

	def get_medics(self):
		medics = Medico.objects.all()
		return medics

	def get_medic_object(self,medicid):
		medic = get_object_or_404(Medico,id=medicid)
		return medic

	def get_medic_event(self,event):
		try:
			medic = Medico.objects.filter(evento_id__in=[events.id for events in event])
		except Exception, e:
			medic = Medico.objects.filter(evento_id=event)
		return medic

	def get_process_medic(self,medicid):
		process = Procedimiento.objects.filter(medico_id__in=[medic.id for medic in medicid])
		return process

	

	def get_process_event_medic(self,eventid,medicid):
		process = {}
		try:
			process = Procedimiento.objects.filter(evento_id__in=[event.id for event in eventid],medico_id__in=[medic.id for medic in medicid])
		except Exception, e:
			process = Procedimiento.objects.filter(evento_id=eventid,medico_id__in=[medic.id for medic in medicid])
		return process

	def get_process_object(self,processid):
		process = get_object_or_404(Procedimiento,id=processid)
		return process

	def get_dx_medic(self,medicid):
		dx = Dx.objects.filter(medico_id__in=[medic.id for medic in medicid])
		return dx

	def get_dx_event(self,eventid):
		try:
			dx = Dx.objects.filter(evento_id__in=[event.id for event in eventid])
		except Exception, e:
			dx = Dx.objects.filter(evento_id=eventid)
		
		return dx

	def get_dx_object(self,dxid):
		dx = get_object_or_404(Dx,id=dxid)
		return dx

	def get_charge_event(self,eventid):
		try:
			charge = Cargo.objects.filter(evento_id__in=[event.id for event in eventid])
		except Exception, e:
			charge = Cargo.objects.filter(evento_id=eventid)
		return charge

	def get_charge_object(self,chargeid):
		charge = get_object_or_404(Cargo,id=chargeid)
		return charge

	def get_count_claims():
		if usertype == TipoUsuario.ECARESOFT or usertype == TipoUsuario.SUPERUSER:
			return Autorizacion.objects.all().filter(tipoAprobacion='1').count()
		elif usertype == TipoUsuario.MAC:
			locality = Localidad.objects.filter(id__in=[locality_ids.localidad_id for locality_ids in get_locality_user(self.id)])
			event = Evento.objects.filter(proveedor_id__in=[provider.id for provider in get_providers_locality(locality)])
			return Autorizacion.objects.all().filter(tipoAprobacion='1',evento_id__in=[events.id for events in event]).count()


	def get_count_invoices():
		if usertype == TipoUsuario.ECARESOFT or usertype == TipoUsuario.SUPERUSER:
			return Autorizacion.objects.all().filter(tipoAprobacion='2').count()
		elif usertype == TipoUsuario.MAC:
			locality = Localidad.objects.filter(id__in=[locality_ids.localidad_id for locality_ids in get_locality_user(self.id)])
			emisor = Emisor.objects.filter(rfc__in=[provider.rfc for provider in get_providers_locality(locality)])
			comprobantes = Comprobante.objects.filter(emisor_id__in=[trans.id for trans in emisor])
			return Autorizacion.objects.all().filter(tipoAprobacion='1',evento_id__in=[events.id for events in event]).count()

	def get_missing_claims():
		if usertype == TipoUsuario.ECARESOFT or usertype == TipoUsuario.SUPERUSER:
			return Autorizacion.objects.all().filter(estatus__in=['E','R'],tipoAprobacion='1').count()
		elif usertype == TipoUsuario.MAC:
			locality = Localidad.objects.filter(id__in=[locality_ids.localidad_id for locality_ids in get_locality_user(self.id)])
			event = Evento.objects.filter(proveedor_id__in=[provider.id for provider in get_providers_locality(locality)])
			return Autorizacion.objects.all().filter(estatus__in=['E','R'],tipoAprobacion='1',evento_id__in=[events.id for events in event]).count()

	def get_missing_invoices():
		if usertype == TipoUsuario.ECARESOFT or usertype == TipoUsuario.SUPERUSER:
			return Autorizacion.objects.all().filter(estatus__in=['E','R'],tipoAprobacion='2').count()


	def get_date(self):
		return self.start,self.end
	

	def set_date(self,start,end):
		self.start = start
		self.end = end



	def set_userid(self,id):
		self.id = id

	def filters(self,queryset,field,objects):
		queryset = queryset.filter(field=objects)
		return queryset

	def set_auth_event(self,id,status,comment,cause):
		Autorizacion.objects.filter(evento_id=id).update(Estado=status,Comentarios=comment,motivo=cause)




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










