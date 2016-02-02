import json
import random
import string
from django.core import serializers
from django.db import connection
from .queries import search
from whatsapp import Client
from pytg.sender import Sender
import requests
import django
from django.conf import settings
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import base64



ESCAPE_STRING_SEQUENCES = (
    (' AND ', '&'),
    (' OR ', '|'),
    ('+', '&'),
)

def get_url(hostname, route):
    return "http://%s/%s" % (hostname, route)


def raw_sql_search(query, pac_id):
    cursor = connection.cursor()

    for sequence in ESCAPE_STRING_SEQUENCES:
        replace_this, for_this = sequence
        query = query.replace(replace_this, for_this)

    params = []

    for i in range(0,6):
        params += [query, pac_id, query]

    cursor.execute(search.RAW_SQL, params)

    result = [{
        'tipo': row[0],
        'id': row[1],
        'highlight': row[2],
        'fecha': row[3],
    } for row in cursor.fetchall()]

    return result

def secret_key_gen():
    return "".join([random.SystemRandom().choice(string.digits 
        + string.letters) for i in xrange(32)])

def sendWhatsapp(**kwargs):
    client = Client(login='5218348538420', password='s2znFNoSU7MabzuFHx3qNXaphbY=')
    for key in kwargs:
        client.send_message(key, kwargs[key])

def sendTelegram(**kwargs):
    sender = Sender("127.0.0.1", port=4458)
    for key in kwargs:
        sender.send_msg(key,unicode(kwargs[key]))

def sendSMS(**kwargs):
    for key in kwargs:
        print('entro SMS')
        payload = {'usuario':'gvaldez','password':'de434a'}
        payload['celular']='+'+str(key)
        payload['mensaje']=kwargs[key]
        r = requests.get("https://www.masmensajes.com.mx/wss/smsapi13.php", params=payload)
        
# def sendEmail(**kwargs):
#     if not kwargs:
#         print('entro sendemail')
#         fromaddr = "facturacion@ecaresoft.com"
#         passmail = "3031393730"
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#         server.login(fromaddr, passmail)
#         for key in kwargs:
#             toaddr = key
#             msg = MIMEMultipart()
#             msg['From'] = fromaddr
#             msg['To'] = key
#             msg['Subject'] = "Estado de Cuenta por revisar"
#             body = kwargs[key]
#             msg.attach(MIMEText(body, 'plain'))
#             text = msg.as_string()
#             server.sendmail(fromaddr, toaddr, text)
        
#         server.quit()

def sendEmail(**kwargs):
    from django.conf import settings
    service = settings.SERVICE_GMAIL
    for key in kwargs:
        try:
           bodyTxt = MIMEText(kwargs[key])
           bodyTxt['subject'] = "Estado de Cuenta por revisar"
           bodyTxt['to'] = key
           bodyTxt['from'] = settings.EMAIL_ACCOUNT
           bodyMsg = {'raw': base64.urlsafe_b64encode(bodyTxt.as_string())}
           aviso = (service.users().messages().send(userId='me', body=bodyMsg).execute())
           print ('Correo enviado. Email Id: %s' % aviso['id'])
           retVal='exitoso'
        except Exception as e:
           print(e)
           retVal='error'
        finally:        
           return retVal

def sendNotifications(localidad, mensaje, tipo):
    localidad = Localidad.objects.get(nombre=localidad)
    usuariosLoc = UsuarioLocalidad.objects.filter(localidad_id=localidad.id)
    paramsWA = {}
    paramsTG = {}
    paramsSMS = {}
    paramsEmail = {}
    for userLoc in usuariosLoc:
        userData = TipoUsuario.objects.get(user_id=userLoc.usuario_id)
        if userData.tipo==tipo:
            if userData.email:
                paramsEmail[userData.email]=mensaje
            if userData.celular:
                if userData.whatsapp == 'Y':
                    paramsWA[userData.celular]=mensaje
                if userData.telegram == 'Y':
                    paramsTG[userData.tgContact]=mensaje
                if userData.sms == 'Y':
                    paramsSMS[userData.celular]=mensaje
    sendWhatsapp(**paramsWA)
    sendTelegram(**paramsTG)
    sendSMS(**paramsSMS)
    sendEmail(**paramsEmail)
