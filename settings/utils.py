from claims.models import *
from django.shortcuts import get_object_or_404, get_list_or_404
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

	def permission(self,typeUser):
		permission = False
		if typeUser == TipoUsuario.ECARESOFT or typeUser == TipoUsuario.SUPERUSER:
			permission = True
		return permission