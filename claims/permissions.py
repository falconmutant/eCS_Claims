from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from .models import *
from .serializers import *

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        #print(obj.owner)
        print(request.data)
        #return obj.owner == request.user
        return True

class ProveedorView(APIView):
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    authentication_classes = (TokenAuthentication, )

    def get_create_prov(self, rfc, request):
        try:
            prov_data = request.data.get('Proveedor')
            prov = Proveedor.objects.get(rfc=rfc,localidad=prov_data.get('localidad'))
        except Proveedor.DoesNotExist:
            provSerial = ProveedorSerializer(data=request.data.get('Proveedor'))
            errors = {}
            if provSerial.is_valid(raise_exception=True):
                prov = provSerial.save()
		
        self.check_object_permissions(self.request, prov)
        return prov

    def get_prov(self, rfc):
        try:
            prov = Proveedor.objects.get(rfc=rfc)
        except Proveedor.DoesNotExist:
            raise Http404("El proveedor no tiene eventos registros en la plataforma")
        
        self.check_object_permissions(self.request, prov)
        return prov

class EventoView(ProveedorView):
    def get_evento(self, evt):
        evento = prov = get_object_or_404(Evento, id=evt)
        return evento

class AppView(APIView):
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)
    authentication_classes = (TokenAuthentication, )
