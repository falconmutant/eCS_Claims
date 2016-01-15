from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Emisor)
admin.site.register(Receptor)
admin.site.register(TimbreFiscal)
admin.site.register(Comprobante)
admin.site.register(Conceptos)
admin.site.register(Impuesto)
admin.site.register(ComprobanteEvento)