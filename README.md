# eCS_Claims
Plataforma de Facturacion 

## Definicion de Endpoints
<table>
<tr><th> Metodo </th><th> Endpoint </th><th> Uso </th><th> Retorno </th></tr>
<tr><td> POST </td><td><a href="#enviarclaim">/proveedores/{RFC}/eventos</a> </td><td> Enviar Reclamacion </td><td> ID de la reclamacion enviada </td></tr>
<tr><td> GET </td><td><a href="#consultarclaim">/proveedores/{RFC}/eventos/{claimID}</a> </td><td> Consultar Reclamacion </td><td> Estatus de la reclamacion </td></tr>
</table>


##EnviarClaim
Enviar un reclamo desde las aplicaciones autorizadas a la plataforma

###Endpoint
```
/proveedores/{RFC}/eventos
```
####Parametros
<table>
<tr><th> Parametro </th><th> Tipo </th><th> Valor </th></tr>
<tr><td colspan="3"> Proveedor </td></tr>
<tr><td> rfc </td><td> String </td><td> RFC del Proveedor de la RED Medica que envia. </td></tr>
<tr><td> cliente </td><td> String </td><td> RED Medica {PEMEX por default} </td></tr>
<tr><td> org </td><td> String</td><td> Zona geografica del Proveedor (Zona Centro, Zona Sur, etc)</td></tr>
<tr><td> hospital </td><td> String </td><td> Nombre de Unidad Medica donde se realizo el evento </td></tr>
<tr><td> localidad </td><td> String</td><td> Localidad donde se realizo el evento </td></tr>
<tr><td colspan="3"> Cuenta </td></tr>
<tr><td> numEvento </td><td> String </td><td> Una descripcion breve del motivo del evento </td></tr>
<tr><td> fechaAdm </td><td> String, formato “yyyy-mm-ddTHH:MM:SSZ” </td><td> Fecha en que inicio el evento </td></tr>
<tr><td> fechaAlta </td><td> String, formato “yyyy-mm-ddTHH:MM:SSZ” </td><td> Fecha en que termino el evento </td></tr>
<tr><td> Total </td><td> Number </td><td> Total del evento (hasta 2 decimales)</td></tr>
<tr><td> cedula </td><td> String </td><td> Cedula del medico responsable del evento </td></tr>
<tr><td> medico </td><td> String </td><td> Nombre del medico responsable del evento </td></tr>
<tr><td> tipo </td><td> String, “C”, “A”, “H”</td><td> Tipo de evento: <b>C</b>onsulta, <b>A</b>mbulatoriom <b>H</b>ospitalizacion </td></tr>
<tr><td> estatus </td><td> String, “A”, “C”</td><td> Estatus del evento: <b>A</b>bierto, <b>C</b>errado </td></tr>
<tr><td colspan="3"> Paciente </td></tr>
<tr><td> curp </td><td> String </td><td> CURP del Paciente</td></tr>
<tr><td> fichaEmp </td><td> String </td><td> Ficha del empleado [PEMEX] </td></tr>
<tr><td> numCod </td><td> String </td><td> Numero de codificacion del empleado [PEMEX] </td></tr>
<tr><td> numEmpresa </td><td> String </td><td> Numero de empresa del empleado [PEMEX] </td></tr>
<tr><td> folioVigencia </td><td> String </td><td> Folio de consulta de vigencia de derechos [PEMEX]  </td></tr>
<tr><td> nombre </td><td> String </td><td> Nombre  del empleado [PEMEX] </td></tr>
<tr><td colspan="3"> listaDx </td></tr>
<tr><td> sistema </td><td> String </td><td> Sistema de codificacion utilizado (CIE-9, CIE10, etc)</td></tr>
<tr><td colspan="3"> dx [LISTA .. N] </td></tr>
<tr><td> curp </td><td> String </td><td> CURP del Paciente</td></tr>
<tr><td> curp </td><td> String </td><td> CURP del Paciente</td></tr>
<tr><td> curp </td><td> String </td><td> CURP del Paciente</td></tr>
<tr><td> curp </td><td> String </td><td> CURP del Paciente</td></tr>

</table>

JSON Ejemplo
```javascript
{
    "medico": "Dr Ismael Tamez Lopez",
    "cedula": "465146113165",
    "especialidad": "NA",
    "tipo": "C",
    "fechaInicio": "2015-12-01T08:00:00Z",
    "fechaFin": "2015-12-01T09:00:00Z",
    "motivo": "Estudio de laboratorio",
    "tomas": [
        {
            "fecha": "2015-12-01T08:15:00Z",
            "signos": [
                {
                    "nombre": "Peso",
                    "valor": 60.0,
                    "unidad": "kg"
                }
            ]
        }
    ],
    "intervenciones": [
        {
            "fecha": "2015-12-01T09:00:00Z",
            "nombre": "Colecistectomia laparoscopica",
            "codigo": "51.23"
        }
    ],
    "recetas": [
        {
          "notas": "evitar bebidas frías, y alimentos irritantes",
          "fecha": "2015-12-01T08:30:00Z",
          "medicamentos": [
              {
                  "via": "oral",
                  "nombre": "Ibuprofeno 400mg",
                  "codigo": "66-10-00-20-00-03-20",
                  "clasificacion": "GPI",
                  "via": "oral",
                  "indicacion": "cada 6 hrs x 5 días",
                  "dosis": "1 tableta"
              }
          ]
      }
    ],
    "diagnosticos": [
        {
            "fecha": "2015-12-01T09:00:00Z",
            "nombre": "Dolor de garganta y en el pecho",
            "codigo": "R07"
        }
    ],
    "cuestionarios": [
        {
            "titulo": "Patologicos",
            "fecha": "2015-12-01T09:00:00Z",
            "preguntas": [
                {
                    "titulo": "Patologicos",
                    "pregunta": "Diabetes?",
                    "respuesta": "true",
                    "descripcion": "Tipo 1"
                }
            ]
        }
    ]
}
```

Respuesta
```javascript
{
    "msj": "Evento creado",
    "id": 1,
    "url": "http://HOST_NAME/pacientes/GOTA750512MGDRA01/eventos/1"
}
```

### Evento
* URL: `/pacientes/{curp}/eventos/{evento_id}`
* GET: _Ver datos completos (Diagnosticos, Intervenciones, etc.) de un Evento_

Parametros

-

Respuesta
```javascript
{
    "id": 1,
    "medico": "Dr Ismael Tamez Lopez",
    "cedula": "465146113165",
    "especialidad": "NA",
    "tipo": "C",
    "fechaInicio": "2015-12-01T08:00:00Z",
    "fechaFin": "2015-12-01T09:00:00Z",
    "motivo": "Estudio de laboratorio",
    "paciente": 1,
    "tomas": [
        {
            "id": 1,
            "fecha": "2015-12-01T08:15:00Z",
            "evento": 1,
            "paciente": 1,
            "signos": [
                {
                    "id": 1,
                    "valor": 60.0,
                    "nombre": "Peso",
                    "unidad": "kg",
                    "toma": 1
                }
            ]
        }
    ],
    "recetas": [
        {
            "id": 1,
            "fecha": "2015-12-01T08:30:00Z",
            "notas": "evitar bebidas frías, y alimentos irritantes",
            "evento": 1,
            "paciente": 1,
            "medicamentos": [
                {
                    "id": 1,
                    "nombre": "Ibuprofeno 400mg",
                    "codigo": "66-10-00-20-00-03-20",
                    "clasificacion": "GPI",
                    "via": "oral",
                    "dosis": "1 tableta",
                    "indicacion": "cada 6 hrs x 5 días",
                    "receta": 1,
                    "paciente": 1
                }
            ]
        }
    ],
    "diagnosticos": [
        {
            "id": 1,
            "fecha": "2015-12-01T09:00:00Z",
            "nombre": "Dolor de garganta y en el pecho",
            "codigo": "R07",
            "evento": 1,
            "paciente": 1
        }
    ],
    "intervenciones": [
        {
            "id": 1,
            "fecha": "2015-12-01T09:00:00Z",
            "nombre": "Colecistectomia laparoscopica",
            "codigo": "51.23",
            "evento": 1,
            "paciente": 1
        }
    ],
    "cuestionarios": [
        {
            "id": 1,
            "titulo": "Patologicos",
            "fecha": "2015-12-01T09:00:00Z",
            "preguntas": [
                {
                    "id": 1,
                    "cuestionario": 1,
                    "titulo": "Patologicos",
                    "pregunta": "Diabetes?",
                    "respuesta": "true",
                    "descripcion": "Tipo 1",
                }
            ],
            "evento": 1,
            "paciente": 1
        }
    ]
}
```

TEXTO





