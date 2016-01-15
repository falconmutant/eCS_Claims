from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Proveedor)
admin.site.register(Evento)
admin.site.register(Dx)
admin.site.register(Cargos)
admin.site.register(Medico)
admin.site.register(Procedimientos)
admin.site.register(Motivos)

