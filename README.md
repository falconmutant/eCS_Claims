# eCS Claims
Aplicacion eCS Claims

## Instalacion
- Herramientas requeridas 
- [x] Python 2.7+
- [x] pip
- [x] virtualenv
- [x] postgresql
- [x] python-devel
-Clonar el repositorio
```sh
$ git clone -v binding git@github.com:falconmutant/eCS_Claims.git [NombreDirectorio]
```
- Crear un entorno virtual con virtualenv
```sh
$ virtualenv venv
```
- Activar el entorno virtual creado
```sh
$ source ENV/bin/activate
```
- Entrar al proyecto
```sh
$ cd [NombreDirectorio]
```
- Instalar dependencias de python
```sh
$ pip install -r requirements.txt
```
- Crear la base de datos `claims`
- Configurar los parametros de acceso en  [automatizar proceso]
```sh
$ nano [NombreDirectorio]/ecsclaims/settings.py
```
```
 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'claims',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
```
- Ejecutar las migraciones de BD
```sh
$ python manage.py migrate
```
- Levantar el servidor
```sh
$ python manage.py runserver 0.0.0.0:8000
```

**Dear Programmer:**

When us are writing this code, only we and God we knew how it worked.

Now, God only knows!

So if you are trying to 'optimize' this routine and fail (probably), 
please increase the next counter as a warning to the next colleague.

**total_hours_lost_here = 0**
