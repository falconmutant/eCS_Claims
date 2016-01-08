from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
#from app.permissions import is_app
from .models import *
from .serializers import *
from .utils import raw_sql_search, secret_key_gen, get_url
from .permissions import ProveedorView, EventoView
import json
import datetime 

# Create your views here.
@api_view(['GET'])
def routes(request, format=None):
    rs = [
        'auth/login',
        'apps/token',
        'proveedores',
        'proveedores/{rfc}/',
        'proveedores/{rfc}/eventos',
        'proveedores/{rfc}/eventos/{evento_id}',
    ]

    routes = [get_url(request.get_host(),r) for r in rs]

    return Response({'routes': routes}, status=status.HTTP_200_OK)

@api_view(['GET','POST'])
def login(request, format=None):
    if request.method == 'POST':
        username = request.data.get('username','')
        password = request.data.get('password','')

        if not username or not password:
            return Response({'message': 'Incorrect params'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)
        if not user:
            return Response({'message': 'No such user'}, status=status.HTTP_404_NOT_FOUND)
    else:
        if request.user.is_authenticated():
            user = request.user
        else:
            return Response({'message': 'No params'}, status=status.HTTP_400_BAD_REQUEST)

    token, created = Token.objects.get_or_create(user=user)

    try:
        proveedor = Proveedor.objects.get(owner_id=user.id)
        name = "%s %s" % (proveedor.cliente, proveedor.org)

        return Response({'token': token.key, 'rfc': proveedor.rfc, 'name': name}, status=status.HTTP_200_OK)

    except Proveedor.DoesNotExist:
        return Response({'token': token.key}, status=status.HTTP_200_OK)


class ProveedorSearch(ProveedorView):
    def post(self, request, rfc, format=None):
        proveedor = self.get_prov(rfc)
        query = request.data.get('query','')

        if not query:
            return Response({'message:' 'Missing query parameter'}, status=status.HTTP_400_BAD_REQUEST)

        result = raw_sql_search(query, proveedor.id)

        return Response(result, status=status.HTTP_200_OK)

class ProveedoresView(ProveedorView):
    def get(self, request, rfc, format=None):
        proveedor = self.get_prov(rfc)

        prov_json = ProveedorSerializer(proveedor).data

        return Response(prov_json, status=status.HTTP_200_OK)


class EventosView(ProveedorView):
    def get(self, request, rfc, format=None):
        proveedor = self.get_prov(rfc)
        estatus = request.GET.get('estatus','')
        if estatus :
            eventos = Evento.objects.filter(estatus=estatus)
        else:
            eventos = Evento.objects.filter(proveedor=proveedor.id).order_by('-fechaAlta')
        if not eventos:
            return Response({'warning': 'Proveedor sin eventos'}, status=status.HTTP_204_NO_CONTENT)

        eventosSerial = EventoSerializer(eventos, many=True).data
        return Response(eventosSerial, status=status.HTTP_200_OK)

    def post(self, request, rfc, format=None):
        proveedor = self.get_create_prov(rfc, request)
        
        request_data = request.data.copy()
        eventoData = request_data.get('Cuenta')
        eventoData['proveedor'] = proveedor.id
        pacienteData = request_data.get('Paciente')
        dxs = request_data.get('listaDx')
        dxData = dxs.pop('dx', [])
        cargosData = request_data.pop('cargos', [])
        
        eventoSerial = EventoSerializer(data=eventoData)
        errors = {}
        
        if not eventoSerial.is_valid():
            response = {
                'msj': 'Error en los datos del evento',
                'errores': eventoSerial.errors
            }
            return Response(response, status=status.HTTP_200_OK)

        evento = eventoSerial.save()
        if evento:
            pacienteData['evento']=evento.id
        
        pacienteSerial = PacienteSerializer(data=pacienteData)
        if not pacienteSerial.is_valid():
            response = {
                'msj': 'Error en los datos del paciente',
                'errores': pacienteSerial.errors
            }
            return Response(response, status=status.HTTP_200_OK)

        paciente = pacienteSerial.save()
        
        # DX
        if dxData:
            for dx in dxData:
                dx['evento'] = evento.id
                dx['sistema'] = dxs.get('sistema')
            dxSerial = DxSerializer(data=dxData, many=True)

            if not dxSerial.is_valid():
                response = {
                    'msj': 'Error en diagnosticos',
                    'errores': dxSerial.errors
                }
                evento.delete()
                return Response(response, status=status.HTTP_200_OK)

            diag = dxSerial.save()
    
        # Cargos
        if cargosData:
            cargosDxDic ={}
            for cargos in cargosData:
                cargos['evento'] = evento.id
                cargosDxDic[cargos['secuencia']] = cargos.get('cargosDx')

            cargosSerial = CargosSerializer(data=cargosData, many=True)

            if not cargosSerial.is_valid():
                response = {
                    'msj': 'Error en los datos de cargos',
                    'errores': cargosSerial.errors
                }
                evento.delete()
                return Response(response, status=status.HTTP_200_OK)

            cargos = cargosSerial.save()
            if cargos:
                for k, v in cargosDxDic.iteritems():
                    cargosRel = Cargos.objects.get(evento_id=evento.id,secuencia=k)
                    for cargosDx in v:
                         cargosDx['cargo'] = cargosRel.id
                         dxRel = Dx.objects.get(evento_id=evento.id,secuencia=cargosDx['dxRel'])
                         cargosDx['dx'] = dxRel.id

                    cargosDxSerial = CargosDxSerializer(data=v, many=True)
                    if not cargosDxSerial.is_valid():
                        response = {
                        'msj': 'Error en los datos de cargos vs dx',
                        'errores': cargosDxSerial.errors
                        }
                        evento.delete()
                        return Response(response, status=status.HTTP_200_OK)
                    cargosDxSerial.save()
        autorizacion= Autorizacion.objects.create(Estatus="R", FechaSolicitud=datetime.datetime.now(), TipoAprobacion="1",Sistema="Cirrus",evento_id=evento.id)

        

        response = {
            'msj': 'Evento creado',
            'id': evento.id,
            'url': get_url(request.get_host(), "proveedores/%s/eventos/%s" % (proveedor.rfc, evento.id))
        }

        return Response(response, status=status.HTTP_201_CREATED)

# Detalles del evento
class EventoDetailView(EventoView):
    def get(self, request, rfc, evento_id, format=None):
        proveedor = self.get_prov(rfc)
        evento = self.get_evento(evento_id)

        evento_json = EventoSerializer(evento).data
        # paciente
        pac_json = PacienteSerializer(Paciente.objects.get(evento=evento)).data
        evento_json['Paciente'] = pac_json
        # diagnosticos
        dx_json = DxSerializer(Dx.objects.filter(evento=evento), many=True).data
        evento_json['listaDx'] = dx_json
        # cargos
        cargos_json = CargosSerializer(Cargos.objects.filter(evento=evento), many=True).data
        # cargos vs dx
        for cargo_json in cargos_json:
            cargosDxDict = CargosDx.objects.filter(cargo=cargo_json['id'])
            cargosDx_json = CargosDxSerializer(cargosDxDict, many=True).data
            cargo_json['listDx'] = cargosDx_json
        evento_json['cargos'] = cargos_json

        return Response(evento_json, status=status.HTTP_200_OK)
