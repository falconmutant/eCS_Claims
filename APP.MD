# eCS Claims
Aplicacion eCS Claims

## Instalacion
- Instalar Python 2.7+
- Intalar pip + virtualenv
- Clonar el repositorio
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
