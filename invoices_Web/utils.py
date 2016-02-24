from .models import *
from django.shortcuts import get_object_or_404, get_list_or_404
from claims.models import *

class Methods:

	def get_locality_user(self,userid):
		locality = {}
		localityid = UsuarioLocalidad.objects.filter(usuario_id=userid)
		locality = Localidad.objects.filter(id__in=[locality_ids.localidad_id for locality_ids in localityid])
		return locality
	def get_providers_locality(self,locality):
		return Proveedor.objects.filter(localidad__in=[localitys.nombre for localitys in locality])

	def get_provider_company(self,idCompany):
		return get_object_or_404(Proveedor,rfc=idCompany)

	def get_company_provider(self,provider):
		return Emisor.objects.filter(rfc__in=[providers.rfc for providers in provider])

	def get_voucher_company(self,company):
		return Comprobante.objects.filter(emisor_id__in=[companys.id for companys in company])

	def get_typeVoucher_voucher(self,voucher):
		return ComprobanteTipo.objects.filter(comprobante__in=[vouchers.id for vouchers in voucher])

	def get_auth_type(self,usertype,typeVoucher,voucher):
		auth={}
		if usertype == TipoUsuario.MAC:
			if typeVoucher == 'history':
				auth = Autorizacion.objects.all().filter(estatus__in=['A','X','Y','N','P'],tipoAprobacion='2',comprobante_id__in=[vouchers.id for vouchers in voucher])
			else:
				auth = Autorizacion.objects.filter(estatus__in=['E','R'],tipoAprobacion='2',comprobante_id__in=[vouchers.id for vouchers in voucher])
		elif usertype == TipoUsuario.PEMEX:
			if typeVoucher == 'history':
				auth = Autorizacion.objects.all().filter(estatus__in=['X'],tipoAprobacion='2',evento_id__in=[vouchers.id for vouchers in voucher])
			else:
				auth = Autorizacion.objects.filter(estatus__in=['Y','P'],tipoAprobacion='2',evento_id__in=[vouchers.id for vouchers in voucher])
		elif usertype == TipoUsuario.ECARESOFT:
			auth = Autorizacion.objects.filter(estatus__in=['E','R','A','P'],tipoAprobacion='2')
		elif usertype == TipoUsuario.SUPERUSER:
			auth = Autorizacion.objects.filter(estatus__in=['E','R','A','P'],tipoAprobacion='2')
		return auth

	def get_voucher_auth(self,auth):
		return Comprobante.objects.filter(id__in=[auths.comprobante_id for auths in auth])

	def get_company_voucher(self,voucher):
		try:
			return Emisor.objects.filter(id__in=[vouchers.emisor_id for vouchers in voucher])
		except Exception, e:
			return get_object_or_404(Emisor,id=voucher)

	def get_eventVoucher_voucher(self,idVoucher):
		return ComprobanteEvento.objects.filter(comprobante=idVoucher)

	def get_event_provider_exclude(self,idProvider,eventVoucher):
		return Evento.objects.filter(proveedor_id=idProvider).exclude(id__in=[eventVouchers.evento for eventVouchers in eventVoucher])

	def get_event_provider(self,idProvider):
		return Evento.objects.filter(proveedor_id=idProvider)

	def get_patient_event(self,event):
		return Paciente.objects.filter(evento_id__in=[events.id for events in event])

	def get_cause(self):
		return Motivos.objects.all()

	def get_tax_voucher(self,idVoucher):
		return get_object_or_404(Impuesto,comprobante_id=idVoucher)

	def get_auth_filter(self,auth,value,obj):
		if value == 'date':
			auth = auth.filter(fechaSolicitud__range=[self.start, self.end])
		if value == 'status':
			auth = auth.filter(estatus__in=obj)
		if value == 'type':
			auth = auth.filter(tipoAprobacion=obj)
		return auth

	def get_auth_user(self,typeUser):
		if typeUser == TipoUsuario.MAC:
			auth = Autorizacion.objects.all().filter(estatus__in='A',tipoAprobacion='1')
		if typeUser == TipoUsuario.PEMEX:
			auth = Autorizacion.objects.all().filter(estatus__in='Y',tipoAprobacion='1')
		return auth

	def get_voucher_object(self,idVoucher):
		return get_object_or_404(Comprobante,id=idVoucher)

	def get_concepts_voucher(self,idVoucher):
		return Conceptos.objects.filter(comprobante_id=idVoucher)

	def get_date(self):
		return self.start,self.end

	def set_date(self,start,end):
		self.start = start
		self.end = end

	def set_auth_status(self,id,status,comment,cause):
		Autorizacion.objects.filter(comprobante_id=id).update(estatus=status,comentarios=comment,motivo_id=cause)
