from .models import *
from rest_framework import serializers

class ProveedorSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Proveedor
        exclude = ()
        
class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        exclude = ()

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        exclude = ()

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        exclude = ()

class ProcedimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedimiento
        exclude = ()

class DxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dx
        exclude = ()

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargos 
        exclude = ()

class CargosDxSerializer(serializers.ModelSerializer):
    class Meta:
        model = CargosDx 
        exclude = ()