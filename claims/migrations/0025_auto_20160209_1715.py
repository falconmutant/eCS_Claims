# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0024_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='motivos',
            name='is_active',
            field=models.CharField(default='N', max_length=1, choices=[('Y', 'Si'), ('N', 'No')]),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='celular',
            field=models.CharField(blank=True, max_length=14, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{13}$', message="Numero debe ingresarse en formato internacional: '+521999999'. 14 digitos en total.")]),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='email',
            field=models.EmailField(max_length=70, blank=True),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='sms',
            field=models.CharField(default='N', max_length=1, choices=[('Y', 'Si'), ('N', 'No')]),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='telegram',
            field=models.CharField(default='N', max_length=1, choices=[('Y', 'Si'), ('N', 'No')]),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='tgcontacto',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='whatsapp',
            field=models.CharField(default='N', max_length=1, choices=[('Y', 'Si'), ('N', 'No')]),
        ),
        migrations.AddField(
            model_name='tipousuario',
            name='celular',
            field=models.CharField(blank=True, max_length=14, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{13}$', message="Numero debe ingresarse en formato internacional: '+521999999'. 14 digitos en total.")]),
        ),
        migrations.AddField(
            model_name='tipousuario',
            name='email',
            field=models.EmailField(max_length=70, blank=True),
        ),
        migrations.AddField(
            model_name='tipousuario',
            name='sms',
            field=models.CharField(default='N', max_length=1, choices=[('Y', 'Si'), ('N', 'No')]),
        ),
        migrations.AddField(
            model_name='tipousuario',
            name='telegram',
            field=models.CharField(default='N', max_length=1, choices=[('Y', 'Si'), ('N', 'No')]),
        ),
        migrations.AddField(
            model_name='tipousuario',
            name='tgcontacto',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='tipousuario',
            name='whatsapp',
            field=models.CharField(default='N', max_length=1, choices=[('Y', 'Si'), ('N', 'No')]),
        ),
        migrations.DeleteModel(
            name='Localidades',
        ),
        migrations.DeleteModel(
            name='TipoUsuarioLocalidades',
        ),
    ]
