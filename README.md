# eCS_Claims
Plataforma de Facturacion 

## Instalacion
1. Instalar Python 2.7+
2. Intalar pip + virtualenv
3. Crear un nuevo virtualenv
```sh
$ virtualenv ENV
```
4. Activar el virtualenv
```sh
$ source ENV/bin/activate
```
5. Instalar dependencias de python
```sh
$ pip install -r requirements.txt
```
6. Actualizar el archivo Settings.py con los valores de conexion para BD [Pendiente automatizar por script]
7. Iniciar  servidor
```sh
$ ./manage.py runserver 0.0.0.0:[PORT]
```

## Definicion de Endpoints
<table>
<tr><th> Metodo </th><th> Endpoint </th><th> Uso </th><th> Retorno </th></tr>
<tr><td> POST </td><td><a href="#enviarclaim">/proveedores/{RFC}/eventos</a> </td><td> Enviar Reclamacion </td><td> ID de la reclamacion enviada </td></tr>
<tr><td> GET </td><td><a href="#consultarclaim">/proveedores/{RFC}/eventos/{claimID}</a> </td><td> Consultar Reclamacion </td><td> Estatus de la reclamacion </td></tr>
</table>

* POST _Crear un evento al Paciente_
##EnviarClaim
Parametros

Tabla
<table>
<tr><th> Parametro </th><th> Tipo </th><th> Descripcion </th></tr>
<tr><td> medico </td><td> String </td><td> Nombre completo del Medico </td></tr>
<tr><td> cedula </td><td> String </td><td> Cedula profesional del Medico </td></tr>
<tr><td> especialidad </td><td> String </td><td> Especialidad del Medico </td></tr>
<tr><td> tipo </td><td> String, “C”, “A”, “H” o "U" </td><td> Tipo de evento: <b>C</b>onsulta, <b>A</b>mbulatorio, <b>H</b>ospitalizacion o <b>U</b>rgencia </td></tr>
<tr><td> fechaInicio </td><td> String, formato “yyyy-mm-ddTHH:MM:SSZ” </td><td> Fecha en que se comenzo el evento </td></tr>
<tr><td> fechaFin </td><td> String, formato “yyyy-mm-ddTHH:MM:SSZ” </td><td> Fecha en que se finalizo el evento </td></tr>
<tr><td> motivo </td><td> String </td><td> Una descripcion breve del motivo del evento </td></tr>
<tr><td> tomas </td><td> N cantidad con la siguiente informacion </td><td> Tomas de signos vitales que se realizaron a lo largo del evento </td></tr>
<tr><td> • fecha </td><td> String, formato “yyyy-mm-ddTHH:MM:SSZ” </td><td> Fecha en que se realizo la toma de signos vitales </td></tr>
<tr><td> • signos </td><td> N cantidad con la siguiente informacion </td><td> Lista de los signos vitales tomados durante esta fecha </td></tr>
<tr><td> &nbsp; ° valor </td><td> Float </td><td> Valor obtenido en la toma de signo vital </td></tr>
<tr><td> &nbsp; ° unidad </td><td> String </td><td> Unidad de la toma de signo vital, ej. "KG" </td></tr>
<tr><td> &nbsp; ° nombre </td><td> String </td><td> Nombre del signo vital, ej "Peso" </td></tr>
<tr><td> intervenciones </td><td> N cantidad con la siguiente informacion </td><td> Lista de intervenciones medicas, ej. Cirujias </td></tr>
<tr><td> • fecha </td><td> String, formato “yyyy-mm-ddTHH:MM:SSZ” </td><td> Fecha en que se realizo la intervencion medica </td></tr>
<tr><td> • nombre </td><td> String </td><td> Nombre de la intervencion </td></tr>
<tr><td> • codigo </td><td> String </td><td> Codigo CIE9V3 (ICD9V3) de la intervencion </td></tr>
<tr><td> recetas </td><td> N cantidad con la siguiente informacion </td><td> Recetas medicas  </td></tr>
<tr><td> • fecha </td><td> String, formato “yyyy-mm-ddTHH:MM:SSZ” </td><td> Fecha en que se recetaron los medicamentos </td></tr>
<tr><td> • nota </td><td> String </td><td> Indicaciones extra sobre la receta medica </td></tr>
<tr><td> • medicamentos </td><td> N cantidad con la siguiente informacion </td><td> Lista de medicamentos de la Receta </td></tr>
<tr><td> &nbsp; ° nombre </td><td> String </td><td> Nombre de medicamento </td></tr>
<tr><td> &nbsp; ° codigo </td><td> String </td><td> Codigo de indentificacion del medicamento </td></tr>
<tr><td> &nbsp; ° clasificacion </td><td> String </td><td> Clasificacion del codigo, ej. "GPI" o "NDC" </td></tr>
<tr><td> &nbsp; ° indicacion </td><td> String </td><td> Indiicaciones sobre frequencia </td></tr>
<tr><td> &nbsp; ° via </td><td> String </td><td> Via de adminstracion </td></tr>
<tr><td> &nbsp; ° dosis </td><td> String </td><td> Dosis del medicamento </td></tr>
<tr><td> diagnosticos </td><td> N cantidad con la siguiente informacion </td><td> Diagnosticos del Paciente </td></tr>
<tr><td> • fecha </td><td> String, formato “yyyy-mm-ddTHH:MM:SSZ” </td><td> Fecha en que se realizo el diagnostico </td></tr>
<tr><td> • nombre </td><td> String </td><td> Nombre del diagnostico </td></tr>
<tr><td> • codigo </td><td> String </td><td> Codigo de CIE10 (ICD10CM6) del padecimiento </td></tr>
<tr><td> cuestionarios </td><td> N cantidad con la siguiente informacion </td><td> Cuestionarios del paciente </td></tr>
<tr><td> • titulo </td><td> String </td><td> Titulo del cuestionario, las preguntas se agrupan mediante esto </td></tr>
<tr><td> • fecha </td><td> String, formato “yyyy-mm-ddTHH:MM:SSZ” </td><td> Titulo del cuestionario </td></tr>
<tr><td> • preguntas </td><td> N cantidad con la siguiente informacion </td><td> Lista de preguntas del cuestionario </td></tr>
<tr><td> &nbsp; ° titulo </td><td> String </td><td> Titulo especifico de la pregunta </td></tr>
<tr><td> &nbsp; ° pregunta </td><td> String </td><td> Pregunta </td></tr>
<tr><td> &nbsp; ° respuesta </td><td> String </td><td> Respuesta </td></tr>
<tr><td> &nbsp; ° descripcion </td><td> String </td><td> Detalles extra de la respuesta a la pregunta </td></tr>

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





