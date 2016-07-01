# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videorsdb', '0002_auto_20160701_1958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='canal',
            name='duenio_de_canal',
        ),
        migrations.RemoveField(
            model_name='subscriptores',
            name='id_canal',
        ),
        migrations.RemoveField(
            model_name='subscriptores',
            name='subscriptor',
        ),
        migrations.RemoveField(
            model_name='downloadvideo',
            name='id_c',
        ),
        migrations.AddField(
            model_name='perfil',
            name='subscriptores',
            field=models.ForeignKey(to='videorsdb.Perfil', null=True),
        ),
        migrations.DeleteModel(
            name='Canal',
        ),
        migrations.DeleteModel(
            name='Subscriptores',
        ),
    ]
