# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videorsdb', '0013_likeanddislike'),
    ]

    operations = [
        migrations.AddField(
            model_name='canal',
            name='descripcion_canal',
            field=models.CharField(max_length=500, blank=True),
        ),
        migrations.AddField(
            model_name='canal',
            name='portada',
            field=models.FileField(max_length=200, upload_to=b'portada/', blank=True),
        ),
    ]
