from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Proveedor)
admin.site.register(Evento)
admin.site.register(Dx)
admin.site.register(Cargo)
admin.site.register(Medico)
admin.site.register(Procedimiento)
admin.site.register(Motivos)
admin.site.register(TipoUsuario)
admin.site.register(Localidad)
admin.site.register(UsuarioLocalidad)