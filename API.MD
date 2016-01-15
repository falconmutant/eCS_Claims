# eCS_Claims
API Plataforma de Facturacion 

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
<tr><td> secuencia </td><td> Int </td><td> Secuencia del diagnostico</td></tr>
<tr><td> codigo </td><td> String </td><td> Codigo del diagnostico</td></tr>
<tr><td> nombre </td><td> String </td><td> Nombre/Descripcion del diagnostico</td></tr>
<tr><td> estatus </td><td> String, “A”, “I”, “R”</td><td>Estatus del diagnostico: <b>A</b>ctivo, <b>I</b>nactivo <b>R</b>esuelto </td></tr>
<tr><td colspan="3"> cargos </td></tr>
<tr><td> secuencia </td><td> String </td><td> Consecutivo del cargo</td></tr>
<tr><td> fechaApli </td><td> String, formato “yyyy-mm-dd”  </td><td> Fecha de aplicacion del cargo</td></tr>
<tr><td> horaApli </td><td> String, formato “THH:MM:SS”  </td><td>Hora de aplicacion del cargo</td></tr>
<tr><td> codigo </td><td> String </td><td>Identificador del cargo</td></tr>
<tr><td> descripcion </td><td> String </td><td>Descripcion del cargo</td></tr>
<tr><td> udm </td><td> String </td><td>Unidad de medida del cargo</td></tr>
<tr><td> cantidad </td><td> Integer </td><td>Numero de unidades aplicadas</td></tr>
<tr><td> precio </td><td> Number </td><td>Precio del cargo</td></tr>
<tr><td> subtotal </td><td> Number </td><td>Subtotal del cargo(Precio*Cantidad)</td></tr>
<tr><td> iva </td><td> Number </td><td>IVA del cargo</td></tr>
<tr><td> descuento </td><td> Number </td><td> Descuento aplicado a el cargo</td></tr>
<tr><td> total </td><td> Number </td><td>Total del cargo((Precio*Cantidad+IVA)-Descuento)</td></tr>
<tr><td> sistema </td><td> String </td><td>Sistema de codificacion del cargo(CPT - NDC - N/A)</td></tr>
<tr><td> sistemaCodigo </td><td> String </td><td>Codigo en el sistema de codificacion del cargo (99929 - N/A)</td></tr>
<tr><td colspan="3"> cargosDx [LISTA .. N] </td></tr>
<tr><td> dxRel </td><td> Int </td><td> Secuencia del diagnostico relacionado al cargo</td></tr>
</table>

JSON Ejemplo
```javascript
{
  "Paciente": {
    "fichaEmp": "98",
    "numEmpresa": "0",
    "folioVigencia": "0",
    "curp": "VICTALPPRCV376MNIV",
    "numCod": "5",
    "nombre": "TALENS VICENTE ISIDRO"
  },
  "Proveedor": {
    "rfc": "XAXX010101000",
    "cliente": "Pemex",
    "org": "Pemex",
    "hospital": "Pacientes Particulares Externo",
    "localidad": "PACIENTES"
  },
  "Cuenta": {
    "numEvento": "1",
    "fechaAdm": "2016-01-06T13:37:56",
    "fechaAlta": "2016-01-06T13:41:01",
    "folioAut": "EC0000000005",
    "total": 0,
    "estatus": "C",
    "cedula": "684097",
    "medico": "LUIS ANTONIO TORRES  FACUNDO",
    "tipo": "H"
  },
  "cargos": [
    {
      "secuencia": "0",
      "codigo": "108637",
      "descripcion": "PASPAT-NF AMP 5X0.2ML",
      "udm": "AMPOLLETA",
      "precio": 135.5,
      "subtotal": 135.5,
      "iva": 0,
      "descuento": 0,
      "total": 0,
      "cargosDx": [
        {
          "dxRel": 0
        }
      ],
      "fechaApli": "2016-01-06T16:40:00.000Z",
      "horaApli": "06:55",
      "sistema": "N/A",
      "sistemaCodigo": "N/A",
      "cantidad": 1
    }
  ],
  "listaDx": {
    "sistema": "CIE-10",
    "dx": [
      {
        "secuencia": "0",
        "codigo": "X146",
        "nombre": "CONTACTO CON AIRE Y GASES CALIENTES, AREA INDUSTRIAL Y DE LA CONSTRUCCION",
        "estatus": "A"
      }
    ]
  }
}
```

Respuesta
```javascript
{
    "msj": "Evento creado",
    "id": {claimID},
    "url": "http://APPHOST/proveedores/{RFC}/eventos/{claimID}"
}
```

##ConsultarClaim
Consultar el estatus de un reclamo

###Endpoint
```
/proveedores/{RFC}/eventos/{claimID}
```
####Parametros
N/A

Respuesta
```javascript
{
  "id": 29,
  "folioAut": "EC0000000042",
  "numEvento": "29",
  "fechaAdm": "2016-01-09T15:25:57Z",
  "fechaAlta": "2016-01-11T12:47:40Z",
  "cedula": "0123456789",
  "medico": "MEDICO DEMO REDES MEDICAS",
  "tipo": "H",
  "estatus": "C",
  "total": "352.00",
  "proveedor": 3,
  "claim": {
    "Motivo": "N/A",
    "Estatus": "R",
    "Display": "Recibido",
    "Comentarios": null
  },
  "Paciente": {
    "id": 26,
    "curp": "OLGALVW69OECEZ6N88",
    "fichaEmp": "1",
    "numCod": "0",
    "numEmpresa": "0",
    "nombre": "ALVARO RODRIGUEZ OLGA LETICIA",
    "evento": 29
  }
}
```




